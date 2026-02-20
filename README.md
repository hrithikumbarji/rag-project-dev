# 🕉️ GitaGPT — Advanced HyDE-Based RAG for Bhagavad Gita Q&A

> A Context-Grounded Retrieval-Augmented Generation (RAG) API for Exploring the Teachings of the Bhagavad Gita

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)
![Groq](https://img.shields.io/badge/LLM-Llama--3.3--70B-orange)
![Embeddings](https://img.shields.io/badge/Embeddings-all--MiniLM--L6--v2-blue)

---

# 📘 Overview

GitaGPT is an advanced **Retrieval-Augmented Generation (RAG)** system designed to answer Bhagavad Gita–related questions using structured Q&A knowledge and semantic retrieval.

This system combines:

- 🧠 **HyDE (Hypothetical Document Expansion)**
- 🔍 **Semantic Vector Search (ChromaDB)**
- 📊 **Similarity Score Threshold Filtering**
- 🔒 **Strict Context-Constrained Answering**
- ⚡ **FastAPI Backend**
- 💻 **Local GPU Embeddings (Apple MPS Support)**

It is optimized for:

- Conceptual understanding
- Explanation-based learning
- Reduced hallucination
- Deterministic vector storage

---

# 🚀 Key Features

## ✅ 1. HyDE Retrieval Enhancement

Before querying the vector database, the system generates a **hypothetical Gita-style explanation** using an LLM.

This improves semantic recall for abstract spiritual questions like:

- What is true duty?
- How to overcome attachment?
- What is karma yoga?
- What is detachment in action?

Pipeline:

```
User Question → HyDE Expansion → Enhanced Query
```

This bridges modern phrasing with scriptural language.

---

## ✅ 2. Vector Search with Similarity Filtering

Uses:

- `sentence-transformers/all-MiniLM-L6-v2`
- Normalized embeddings
- Cosine similarity
- Configurable similarity threshold

Weak matches are filtered out before response generation, reducing hallucination risk.

---

## ✅ 3. Context-Constrained Answering

The LLM is explicitly instructed to:

- Answer ONLY using retrieved context
- Refuse when information is insufficient
- Avoid external knowledge
- Limit responses to 5–6 lines

This enforces grounded generation.

---

## ✅ 4. Deterministic Embedding Architecture

- SHA256-based IDs prevent duplicate embeddings
- Automatic Chroma persistence
- Batch-based ingestion
- Stable vector IDs for reproducibility

---

# 🏗 Architecture Overview

```
User Question
     ↓
HyDE Expansion (LLM)
     ↓
Enhanced Query = Question + HyDE
     ↓
Vector Search (ChromaDB)
     ↓
Similarity Threshold Filtering
     ↓
Context-Constrained LLM Response
     ↓
Answer + Sources Returned
```

---

# 📂 Project Structure

```
rag-project-dev/
│
├── api/
│   ├── main.py
│   └── __init__.py
│
├── ingest/
|   ├── download_dataset.py
│   ├── clean_dataset.py
│   ├── chunk_dataset.py
│   └── embed_chunks.py
│
├── data/
│   ├── raw.json
│   ├── cleaned.json
│   └── chunk_dataset.json
│
├── chroma_db/
└── README.md
```

---

# 📦 Chunk Format

Structured Q&A storage format:

```json
{
  "text": "Answer text only",
  "metadata": {
    "source_question": "...",
    "source_file": "...",
    "type": "qa_explanation"
  }
}
```

Design goals:

- Question-aware retrieval
- Explanation-focused learning
- Clean metadata tracking
- Scalable toward verse-level upgrades

---

# ⚙️ Installation

## 1️⃣ Create Virtual Environment

macOS / Linux:

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Core dependencies include:

- fastapi
- uvicorn
- langchain
- langchain-chroma
- langchain-groq
- langchain-huggingface
- chromadb
- sentence-transformers
- python-dotenv

---

## 3️⃣ Add Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

# 📊 Data Ingestion Pipeline

## Step 1 — Download Dataset

```bash
python ingest/download_dataset.py
```

## Step 2 — Clean Dataset

```bash
python ingest/clean_dataset.py
```

Transforms raw Q&A into structured format.

---

## Step 3 — Chunk Dataset

```bash
python ingest/chunk_dataset.py
```

Features:

- Avoids over-splitting short answers
- Adds document metadata
- SHA256-based deduplication

---

## Step 4 — Embed into Chroma

```bash
python ingest/embed_chunks.py
```

Features:

- Normalized vectors
- Deterministic vector IDs
- Batch insertion
- Persistent storage

---

# 🖥 Running the API

From project root:

```bash
uvicorn api.main:app --reload
```

If inside `api/` directory:

```bash
uvicorn main:app --reload
```

Interactive API docs:

```
http://127.0.0.1:8000/docs
```
API runs at

```
http://127.0.0.1:8000
```

Start Web UI

```bash
streamlit run app.py
```
UI opens at

```
http://localhost:8501

```
---

# 📡 API Usage

### POST `/ask`

### Request

```json
{
  "question": "What is the meaning of karma yoga?"
}
```

### Response

```json
{
  "answer": "...",
  "hyde_expansion": "...",
  "sources": [
    "Original source question text"
  ]
}
```

---

# 🔒 Hallucination Minimization Strategy

| Technique | Implemented |
|------------|-------------|
| Temperature = 0 | ✅ |
| HyDE expansion | ✅ |
| Similarity threshold filtering | ✅ |
| Context-only answering | ✅ |
| Refusal behavior | ✅ |
| Deterministic embeddings | ✅ |

---

# 🧠 Current System Type

This project currently operates as:

> **Retrieval-Augmented FAQ Assistant for Bhagavad Gita Teachings**

It does **not yet** use verse-level scripture ingestion.

---

# 🚀 Planned Upgrade Path

- Ingest full Sanskrit + English translation
- Add chapter/verse metadata
- Enable precise scripture citation
- Hybrid BM25 + Vector retrieval
- Cross-encoder reranking
- Retrieval confidence scoring
- Self-verification LLM pass
- Async FastAPI optimization
- Docker deployment support

---

# 📈 System Maturity

This implementation includes:

- Multi-step retrieval reasoning
- HyDE-based semantic expansion
- Deterministic embedding architecture
- Structured ingestion pipeline
- Guarded LLM prompting
- GPU-accelerated embeddings

For an MVP devotional AI assistant, this is a robust and scalable foundation.

---

# 👨‍💻 Author

**Hrithik Umbarji**

Built with discipline, devotion, and a passion for spiritual learning.

---

# 🕉️ Guiding Principle

“na hi jñānena sadṛśaṁ pavitram iha vidyate.”  
*There is nothing as purifying as true knowledge.* — Bhagavad Gita 4.38

---

⭐ If this project supports your journey of learning and reflection, consider starring the repository.
