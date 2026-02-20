# 🕉️ GitaGPT — HyDE-Enhanced Grounded RAG

> A High-Trust AI Assistant for Scripturally Grounded Wisdom from the Bhagavad Gita

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)
![Groq](https://img.shields.io/badge/LLM-Llama--3.3--70B-orange)

---

# 🌟 Overview

GitaGPT is an advanced **HyDE-powered Retrieval-Augmented Generation (RAG)** system designed to deliver **accurate, citation-backed, context-grounded wisdom** from the Bhagavad Gita.

Unlike naive RAG systems that rely on a single raw query, GitaGPT combines:

- 🧠 Hypothetical Document Expansion (HyDE)
- 🔍 Enhanced Semantic Retrieval
- 📖 Strict Context-Constrained Answering
- 🏷️ Automatic Chapter & Verse Citation Extraction
- 🔒 Hallucination Minimization via grounded prompts

This ensures responses are:

- ✅ Scripturally Grounded  
- ✅ Semantically Accurate  
- ✅ Hallucination-Resistant  
- ✅ Fully Verifiable  

---

# 🏗️ Project Structure

```text
rag-project-dev/
│
├── ingest/
│   ├── download_dataset.py    # Downloads Bhagavad Gita dataset
│   ├── clean_dataset.py       # Cleans & standardizes raw text
│   ├── chunk_dataset.py       # Splits text into semantic chunks
│   └── embed_chunks.py        # Creates embeddings & stores in ChromaDB
│
├── api/
│   └── main.py                # FastAPI Backend (HyDE + RAG Logic)
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

GitaGPT uses a clean, modular ingestion pipeline:

## 1️⃣ Download Dataset

```bash
python ingest/download_dataset.py
```

## 2️⃣ Clean Dataset

```bash
python ingest/clean_dataset.py
```

- Removes formatting noise  
- Normalizes structure  
- Preserves chapter & verse metadata  

## 3️⃣ Chunk Dataset

```bash
python ingest/chunk_dataset.py
```

- Splits verses into semantically meaningful chunks  
- Retains:
  - chapter
  - verse
  - text  

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

# 🧠 RAG Architecture

## 🔍 Step 1 — HyDE Query Expansion

Before retrieval, the system generates a **hypothetical Bhagavad Gita–style paragraph** based on the user’s question.

Example:

User:
> How do I control stress?

HyDE generates:
> The restless mind, afflicted by worldly agitation, must be steadied through discipline, detachment, and devotion to one’s dharma...

This bridges the gap between:

- Modern vocabulary  
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

- Top 5 semantically similar chunks retrieved from ChromaDB  
- Improved alignment with scriptural language  
- Reduced irrelevant matches  

---

## 📖 Step 3 — Strict Grounded Generation

System constraint:

```
Answer ONLY using the context.
Cite Chapter/Verse if available.
Limit to 5–6 lines.
```

This guarantees:

- No external knowledge
- No speculative additions
- Scripture-grounded responses only

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
- Install all dependencies

---

### ▶️ Activate Virtual Environment

```bash
source activate.sh
```

---

### ⏹️ Deactivate Virtual Environment

```bash
source deactivate.sh
```

---

## 🪟 Windows Setup

`setup.sh` is not supported on Windows.  
Follow manual steps below.

### 1️⃣ Create Virtual Environment

```powershell
python -m venv venv
```

### 2️⃣ Activate Environment

**PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

**Command Prompt (cmd):**

```cmd
venv\Scripts\activate.bat
```

### 3️⃣ Upgrade pip

```powershell
python -m pip install --upgrade pip
```

### 4️⃣ Install Requirements

```powershell
pip install -r requirements.txt
```

### ⏹️ Deactivate (Windows)

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
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

Runs at:

```
http://localhost:8000
```

---

## 5️⃣ Launch Frontend

```bash
streamlit run app.py
```

Runs at:

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

# 🆚 Why This Is Advanced RAG

| Basic RAG | GitaGPT |
|------------|---------|
| Raw user query only | HyDE-expanded query |
| Weak semantic match | Scriptural-style expansion |
| No citation enforcement | Chapter/Verse extraction |
| Loose ingestion script | Structured ETL pipeline |
| Higher hallucination risk | Strict context-only answering |

---

# 🔒 Hallucination Resistance Strategy

- Temperature = 0  
- Context-only answering  
- Citation extraction  
- Controlled response length  
- No external knowledge injection  

---

# 🧘 Example Flow

User asks:

> How do I control my restless mind?

System:

1. Generates HyDE expansion  
2. Retrieves top 5 relevant verses  
3. Extracts Chapter/Verse metadata  
4. Produces grounded 5-line response  
5. Returns citations  

---

# 🌺 Future Improvements

- [ ] LLM-based relevance grader (Self-Correcting RAG)
- [ ] Multi-query expansion (3 variations)
- [ ] Hybrid search (BM25 + Vector)
- [ ] Sanskrit + Transliteration toggle
- [ ] Daily Verse Mode
- [ ] Audio Recitation
- [ ] Mobile App version

---

# 👨‍💻 Author

**Hrithik Umbarji**

Built with discipline, devotion, and reverence for sacred knowledge.

---

# 🕉️ Guiding Principle

“tad viddhi praṇipātena paripraśnena sevayā.”  
*Approach wisdom with humility, inquiry, and service.* — Bhagavad Gita 4.34

---

⭐ If this project helps you learn and reflect, consider starring the repository.
