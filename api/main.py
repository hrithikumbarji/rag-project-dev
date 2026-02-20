from fastapi import FastAPI
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
app = FastAPI(title="GitaGPT Advanced RAG")

# --- Initialize Components ---
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'mps'},
    encode_kwargs={'normalize_embeddings': True}
)

db = Chroma(
    collection_name="gita_collection",
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

# --- Prompts ---
hyde_prompt = ChatPromptTemplate.from_template("""
You are a Vedic scholar. Given the question below, write a short, hypothetical 
paragraph that reflects Bhagavad Gita philosophy. Focus on dharma, karma, detachment, and the soul.

Question: {question}
Hypothetical Answer:
""")

rag_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "Answer strictly using ONLY the provided context. "
     "If the answer is not clearly found in the context, say: "
     "'I do not have enough information in the retrieved teachings.' "
     "Limit response to 5-6 lines."),
    ("human", "Context:\n{context}\n\nQuestion:\n{question}")
])

@app.post("/ask")
def ask(question: str):

    # STEP 1: HyDE Expansion
    hyde_chain = hyde_prompt | llm | StrOutputParser()
    hyde_expansion = hyde_chain.invoke({"question": question})

    # STEP 2: Retrieval with similarity score
    results = db.similarity_search_with_score(
        f"{question} {hyde_expansion}",
        k=5
    )

    # 🔒 Filter weak matches
    SCORE_THRESHOLD = 0.75
    filtered_docs = [doc for doc, score in results if score < SCORE_THRESHOLD]

    if not filtered_docs:
        return {
            "answer": "I do not have enough relevant teachings to answer this question.",
            "hyde_expansion": hyde_expansion,
            "sources": []
        }

    # STEP 3: Extract sources (FAQ question references)
    sources = list(set(
        d.metadata.get("source_question", "Unknown")
        for d in filtered_docs
    ))

    # STEP 4: Final Generation
    context = "\n\n".join(d.page_content for d in filtered_docs)

    messages = rag_prompt.format_messages(
        context=context,
        question=question
    )

    response = llm.invoke(messages)

    return {
        "answer": response.content.strip(),
        "hyde_expansion": hyde_expansion,
        "sources": sources
    }