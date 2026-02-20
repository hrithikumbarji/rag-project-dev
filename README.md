# 🕉️ GitaGPT — Advanced HyDE-Based RAG for Bhagavad Gita Q&A

> A Context-Grounded Retrieval-Augmented Generation (RAG) API + Web UI for Exploring the Teachings of the Bhagavad Gita

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)
![Groq](https://img.shields.io/badge/LLM-Llama--3.3--70B-orange)
![Embeddings](https://img.shields.io/badge/Embeddings-all--MiniLM--L6--v2-blue)

---

# 📘 Overview

GitaGPT is an advanced **Retrieval-Augmented Generation (RAG)** system designed to answer Bhagavad Gita–related questions using structured Q&A knowledge and semantic retrieval.

It includes:

- ⚡ FastAPI backend API
- 💻 Streamlit web interface (`app.py`)
- 🧠 HyDE (Hypothetical Document Expansion)
- 🔍 ChromaDB semantic vector search
- 📊 Similarity score filtering
- 🔒 Strict context-grounded answering
- 🧬 Deterministic embeddings (SHA256 IDs)

The system is optimized for:

- Conceptual understanding
- Explanation-based learning
- Reduced hallucination
- Scalable scripture upgrades

---

# 🚀 Key Features

## 🧠 1. HyDE Retrieval Enhancement

Before querying the vector database, the system generates a **hypothetical Gita-style explanation** using an LLM.

Pipeline:

```
User Question → HyDE Expansion → Enhanced Query
```

This improves retrieval for abstract spiritual queries like:

- What is karma yoga?
- What is detachment?
- What is true duty?
- How to overcome attachment?

---

## 🔍 2. Vector Search with Similarity Filtering

Uses:

- `sentence-transformers/all-MiniLM-L6-v2`
- Normalized embeddings
- Cosine similarity
- Configurable similarity threshold

Weak matches are filtered before generation, reducing hallucination risk.

---

## 🔒 3. Strict Context-Constrained Answering

The LLM is instructed to:

- Answer ONLY using retrieved context
- Refuse when insufficient data
- Avoid external knowledge
- Limit responses to 5–6 lines

This ensures grounded output.

---

## 🧬 4. Deterministic Embedding Architecture

- SHA256-based vector IDs
- Duplicate prevention
- Batch-based ingestion
- Persistent Chroma storage
- Apple Silicon GPU (MPS) support

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
│   └── main.py
│
├── ingest/
│   ├── download_dataset.py
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
│
├── app.py                # Streamlit Web UI
│
├── setup.sh              # Creates venv & installs dependencies
├── activate.sh           # Activates virtual environment
├── deactivate.sh         # Deactivates virtual environment
│
├── requirements.txt
└── README.md
```

---

# 📦 Chunk Format

Structured Q&A chunks are stored in `chunk_dataset.json` as:

```json
{
  "text": "Dhritarashtra is blind, both physically and symbolically — representing ignorance...",
  "metadata": {
    "doc_id": 0,
    "source_question": "Why does Dhritarashtra ask Sanjaya to describe the battlefield?",
    "source_file": "Bhagavad-Gita-QA",
    "chunk_index": 0,
    "total_chunks": 1,
    "type": "qa_explanation"
  }
}
```

Design goals:

- Question-aware retrieval
- Explanation-focused learning
- Clean metadata tracking
- Future upgrade path toward verse-level ingestion

---

# ⚙️ Environment Setup

## 🐧 macOS / Linux (Recommended)

### 1️⃣ Run Automated Setup

```bash
bash setup.sh
```

This will:

- Create `venv/`
- Activate environment
- Upgrade pip
- Install dependencies

### ▶️ Activate Environment

```bash
source activate.sh
```

### ⏹️ Deactivate Environment

```bash
source deactivate.sh
```

---

## 🪟 Windows Setup (Manual)

### 1️⃣ Create Virtual Environment

```powershell
python -m venv venv
```

### 2️⃣ Activate

PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

CMD:

```cmd
venv\Scripts\activate.bat
```

### 3️⃣ Install Dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### ⏹️ Deactivate

```powershell
deactivate
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

Transforms raw Q&A into structured JSON.

## Step 3 — Chunk Dataset

```bash
python ingest/chunk_dataset.py
```

Features:

- Adds doc_id and chunk metadata
- Avoids over-splitting short answers
- SHA256-based deduplication

## Step 4 — Embed into Chroma

```bash
python ingest/embed_chunks.py
```

Features:

- Normalized vectors
- Deterministic IDs
- Batch insertion
- Persistent storage in `chroma_db/`

---

# 🖥 Running the Application

## 1️⃣ Start Backend API

```bash
uvicorn api.main:app --reload
```

API runs at:

```
http://127.0.0.1:8000
```

Interactive docs:

```
http://127.0.0.1:8000/docs
```

---

## 2️⃣ Start Web UI

```bash
streamlit run app.py
```

UI opens at:

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

This system currently operates as:

> **Retrieval-Augmented FAQ Assistant for Bhagavad Gita Teachings**

It does NOT yet use verse-level scripture ingestion.

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
- GPU-ready embedding support
- API + UI interface

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
