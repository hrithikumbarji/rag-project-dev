# 🕉️ GitaGPT — HyDE-Enhanced Grounded RAG

> A High-Trust AI Assistant for Scripturally Grounded Wisdom from the Bhagavad Gita

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)
![Groq](https://img.shields.io/badge/LLM-Llama--3.3--70B-orange)

---

# 🌟 Overview

GitaGPT is an advanced **HyDE-powered Retrieval-Augmented Generation (RAG)** system designed to deliver **accurate, context-grounded wisdom** from the Bhagavad Gita.

Unlike naive RAG systems that rely on a single raw query, GitaGPT uses:

- 🧠 Hypothetical Document Expansion (HyDE)
- 🔍 Enhanced Semantic Retrieval
- 📖 Strict Context-Constrained Answering
- 🏷️ Chapter & Verse Citation Extraction

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
│   ├── ingest.py           # Data processing & Vector DB creation
│   └── chroma_db/          # Generated Vector Store
│
├── api/
│   └── main.py             # FastAPI Backend (HyDE + RAG Logic)
│
├── app.py                  # Streamlit Frontend
├── requirements.txt        # Dependencies
└── .env                    # GROQ API Key
```

---

# 🧠 Architecture

## 🔍 Step 1 — HyDE Query Expansion

Instead of embedding only the user question, GitaGPT first generates a **hypothetical spiritual paragraph** in the style of the Bhagavad Gita.

Example:

User Question:
> How do I control stress?

HyDE Expansion:
> The restless mind, afflicted by worldly agitation, must be restrained through discipline, detachment, and devotion to one’s dharma...

This bridges the gap between:

- Modern language  
- Scriptural terminology  

This technique is called:

> **HyDE (Hypothetical Document Embeddings)**

---

## 📚 Step 2 — Enhanced Semantic Retrieval

We combine:

```
[User Question] + [HyDE Expansion]
```

Then perform similarity search in ChromaDB.

This results in:

- Higher semantic alignment  
- Better verse retrieval  
- Reduced irrelevant matches  

---

## 📖 Step 3 — Strict Grounded Generation

The final answer is generated using:

- Only retrieved verses  
- No external knowledge  
- No speculative additions  

System Prompt Constraint:

```
Answer ONLY using the context.
Cite Chapter/Verse if available.
Limit to 5–6 lines.
```

This ensures grounded, scripture-based responses.

---

# 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| LLM | Llama-3.3-70B (via Groq) |
| Embeddings | all-MiniLM-L6-v2 |
| Vector DB | ChromaDB |
| Backend | FastAPI |
| Frontend | Streamlit |
| Framework | LangChain |

---

# 🚀 Getting Started

## 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2️⃣ Add API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_key_here
```

---

## 3️⃣ Ingest the Bhagavad Gita

```bash
python ingest/ingest.py
```

This creates:

```
ingest/chroma_db/
```

---

## 4️⃣ Start Backend

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

---

## 5️⃣ Launch UI

```bash
streamlit run app.py
```

---

# 🆚 Why This Is Not Naive RAG

| Naive RAG | GitaGPT |
|-----------|---------|
| Raw user query only | HyDE-expanded query |
| Weak semantic match | Scriptural-style expansion |
| Higher hallucination risk | Context-only generation |
| No structured citation | Chapter/Verse extraction |

---

# 🧘 Example Flow

User asks:
> How do I control my restless mind?

System:

1. Generates HyDE expansion
2. Retrieves top 5 relevant verses
3. Extracts Chapter/Verse metadata
4. Produces grounded 5-line response
5. Returns citation list

---

# 🔒 Hallucination Resistance Strategy

- Temperature = 0
- Context-only answering
- No external knowledge injection
- Strict system prompt constraint
- Limited response length

---

# 🌺 Future Improvements

- [ ] Add LLM-based relevance grader (Self-Correcting RAG)
- [ ] Multi-query expansion (3 variations instead of 1 HyDE)
- [ ] Hybrid search (BM25 + Vector)
- [ ] Verse highlighting in UI
- [ ] Daily Verse Mode
- [ ] Audio Recitation
- [ ] Sanskrit + Transliteration Toggle

---

# 👨‍💻 Author

**Hrithik Umbarji**

Crafted with devotion, discipline, and reverence for sacred knowledge.

---

# 🕉️ Guiding Principle

“Yogaḥ karmasu kauśalam.”  
*Excellence in action is Yoga.* — Bhagavad Gita 2.50

---

⭐ If you find this meaningful, please star the repository.
