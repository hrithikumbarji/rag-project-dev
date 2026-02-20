# 🕉️ GitaGPT — HyDE-Enhanced QA Retrieval RAG

> A High-Trust AI Assistant for Learning and Exploring the Wisdom of the Bhagavad Gita

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)
![Groq](https://img.shields.io/badge/LLM-Llama--3.3--70B-orange)

---

# 🌟 Overview

GitaGPT is an advanced **HyDE-powered Retrieval-Augmented Generation (RAG)** system designed to deliver accurate, context-grounded explanations from the Bhagavad Gita.

Instead of retrieving isolated verses, GitaGPT retrieves **structured Question–Answer knowledge chunks**, making it optimized for learning and conceptual understanding.

Unlike naive RAG systems that rely on a single raw query, GitaGPT combines:

- 🧠 Hypothetical Document Expansion (HyDE)
- 🔍 Enhanced Semantic Retrieval
- 📚 Structured Q&A Chunk Retrieval
- 📖 Strict Context-Constrained Answering
- 🔒 Hallucination Minimization via grounded prompts

This ensures responses are:

- ✅ Contextually Accurate  
- ✅ Semantically Aligned with Scripture  
- ✅ Explanation-Oriented  
- ✅ Hallucination-Resistant  

---

# 🏗️ Project Structure

```text
rag-project-dev/
│
├── ingest/
│   ├── download_dataset.py    # Downloads Bhagavad Gita dataset
│   ├── clean_dataset.py       # Cleans & standardizes raw text
│   ├── chunk_dataset.py       # Converts text into structured Q&A chunks
│   └── embed_chunks.py        # Creates embeddings & stores in ChromaDB
│
├── api/
│   └── main.py                # FastAPI Backend (HyDE + Retrieval Logic)
│
├── app.py                     # Streamlit Frontend
│
├── setup.sh                   # Creates venv & installs dependencies (macOS/Linux)
├── activate.sh                # Activates virtual environment
├── deactivate.sh              # Deactivates virtual environment
│
├── requirements.txt
└── .env
```

---

# 🔄 Data Ingestion Pipeline (Structured ETL)

GitaGPT follows a clean and modular ingestion workflow.

## 1️⃣ Download Dataset

```bash
python ingest/download_dataset.py
```

## 2️⃣ Clean Dataset

```bash
python ingest/clean_dataset.py
```

- Removes formatting noise  
- Normalizes text  
- Prepares data for structured processing  

## 3️⃣ Chunk Dataset (Q&A Structured)

```bash
python ingest/chunk_dataset.py
```

This converts the dataset into structured Question–Answer chunks optimized for retrieval.

## 4️⃣ Embed & Store

```bash
python ingest/embed_chunks.py
```

- Uses `all-MiniLM-L6-v2`
- Stores embeddings in **ChromaDB**
- Creates persistent vector store:

```
ingest/chroma_db/
```

---

# 📦 Chunk Format

Chunks are stored as structured Q&A objects:

```json
{
  "text": "Question: ... Answer: ...",
  "metadata": {
    "source_question": "...",
    "chunk_index": 0,
    "total_chunks": 1
  }
}
```

This means retrieval is:

- Question-aware  
- Context-preserving  
- Explanation-focused  

Instead of retrieving raw verses, GitaGPT retrieves **pre-structured explanatory knowledge units**.

---

# 🧠 RAG Architecture

## 🔍 Step 1 — HyDE Query Expansion

Before retrieval, the system generates a **hypothetical Gita-style explanation** based on the user's question.

Example:

User:
> How do I control stress?

HyDE generates:
> The restless mind, disturbed by worldly agitation, must be steadied through discipline and detachment...

This bridges the gap between:

- Modern language  
- Scriptural terminology  

Technique used:

> **HyDE (Hypothetical Document Embeddings)**

---

## 📚 Step 2 — Enhanced Semantic Retrieval

Search Query:

```
User Question + HyDE Expansion
```

Then:

- Top 5 semantically similar Q&A chunks retrieved from ChromaDB  
- Improved alignment with spiritual vocabulary  
- Reduced irrelevant matches  

---

## 📖 Step 3 — Context-Grounded QA Generation

System constraint:

```
Answer ONLY using the context.
Limit to 5–6 lines.
```

This guarantees:

- No external knowledge  
- No speculation  
- Answer derived strictly from retrieved Q&A chunks  

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

### ▶️ Activate

```bash
source activate.sh
```

### ⏹️ Deactivate

```bash
source deactivate.sh
```

---

## 🪟 Windows Setup

`setup.sh` is not supported on Windows.

### 1️⃣ Create Virtual Environment

```powershell
python -m venv venv
```

### 2️⃣ Activate

PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

Command Prompt:

```cmd
venv\Scripts\activate.bat
```

### 3️⃣ Install Requirements

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### ⏹️ Deactivate

```powershell
deactivate
```

---

# 🚀 Running the Application

## 1️⃣ Activate Environment

macOS / Linux:

```bash
source activate.sh
```

Windows:

```powershell
venv\Scripts\Activate.ps1
```

---

## 2️⃣ Add API Key

Create `.env` file:

```env
GROQ_API_KEY=your_key_here
```

---

## 3️⃣ Run Ingestion (First Time Only)

macOS / Linux:

```bash
python ingest/download_dataset.py
python ingest/clean_dataset.py
python ingest/chunk_dataset.py
python ingest/embed_chunks.py
```

Windows:

```powershell
python ingest\download_dataset.py
python ingest\clean_dataset.py
python ingest\chunk_dataset.py
python ingest\embed_chunks.py
```

---

## 4️⃣ Start Backend

```bash
uvicorn api.main:app --reload
```

API runs at:

```
http://127.0.0.1:8000
```

---

## 5️⃣ Launch Frontend

```bash
streamlit run app.py
```

UI runs at:

```
http://localhost:8501
```

---

# 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| LLM | Llama-3.3-70B (Groq) |
| Embeddings | all-MiniLM-L6-v2 |
| Vector Store | ChromaDB |
| Backend | FastAPI |
| Frontend | Streamlit |
| Framework | LangChain |

---

# 🆚 Why This Is More Advanced Than Basic RAG

| Basic RAG | GitaGPT |
|------------|---------|
| Raw user query only | HyDE-expanded query |
| Generic document chunks | Structured Q&A chunks |
| Weak semantic match | Scriptural-style expansion |
| Loose ingestion | Clean ETL pipeline |
| Higher hallucination risk | Strict context-only answering |

---

# 🔒 Hallucination Resistance Strategy

- Temperature = 0  
- Context-only answering  
- Limited output length  
- No external knowledge injection  
- Retrieval from curated Q&A chunks  

---

# 🧘 Example Flow

User asks:

> Why does Dhritarashtra ask Sanjaya to describe the battlefield?

System:

1. Generates HyDE expansion  
2. Retrieves relevant Q&A chunk  
3. Uses only retrieved explanation  
4. Produces concise grounded answer  

---

# 🌺 Future Improvements

- [ ] Add chapter/verse metadata support
- [ ] Implement LLM-based relevance grading
- [ ] Hybrid search (BM25 + Vector)
- [ ] Sanskrit + Transliteration toggle
- [ ] Daily Learning Mode
- [ ] Audio Recitation
- [ ] Mobile App version

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
