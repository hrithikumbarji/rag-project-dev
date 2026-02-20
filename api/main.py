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
    model_kwargs={'device': 'mps'}  # Uses your Mac's GPU
)

db = Chroma(
    collection_name="gita_collection",
    persist_directory="./ingest/chroma_db",
    embedding_function=embeddings
)

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

# --- Prompts ---
# 1. HyDE Prompt: Generates a "hypothetical" Gita-style answer to improve retrieval
hyde_prompt = ChatPromptTemplate.from_template("""
You are a Vedic scholar. Given the question below, write a short, hypothetical 
paragraph that sounds like it came from the Bhagavad Gita or its commentary. 
Focus on spiritual concepts like dharma, karma, and the soul to help find relevant verses.

Question: {question}
Hypothetical Answer:""")

# 2. Final RAG Prompt: Grounded answer based strictly on retrieved context
rag_prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer ONLY using the context. Cite Chapter/Verse if available. Limit to 5-6 lines."),
    ("human", "Context:\n{context}\n\nQuestion:\n{question}")
])

@app.post("/ask")
def ask(question: str):
    # STEP 1: HyDE Expansion
    hyde_chain = hyde_prompt | llm | StrOutputParser()
    hyde_expansion = hyde_chain.invoke({"question": question})

    # STEP 2: Enhanced Retrieval
    # We search using a combined query for maximum semantic coverage
    search_query = f"{question} {hyde_expansion}"
    docs = db.similarity_search(search_query, k=5)

    if not docs:
        return {"answer": "No relevant verses found.", "expansion": hyde_expansion, "sources": []}

    # STEP 3: Source Metadata Extraction
    # Extract Chapter/Verse (assumes these keys exist in your metadata)
    sources = []
    for d in docs:
        c, v = d.metadata.get('chapter'), d.metadata.get('verse')
        if c and v:
            sources.append(f"Ch {c}, Verse {v}")
    
    # STEP 4: Final Generation
    context = "\n\n".join(d.page_content for d in docs)
    messages = rag_prompt.format_messages(context=context, question=question)
    response = llm.invoke(messages)

    return {
        "answer": response.content.strip(),
        "hyde_expansion": hyde_expansion,
        "sources": list(set(sources))  # Remove duplicates
    }