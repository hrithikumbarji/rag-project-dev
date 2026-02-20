# 🕉️ GitaGPT: Advanced Spiritual RAG

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/LLM-Llama_3.3_70B-orange?style=for-the-badge)](https://groq.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

An advanced AI assistant that provides grounded, verified wisdom from the **Bhagavad Gita** using a self-correcting RAG pipeline. Built to run efficiently on local machines (like 8GB Macs) while leveraging cloud-scale LLMs.

---

## ✨ Key Features

### 🔍 Path A: Multi-Query Expansion
GitaGPT doesn't just search for your words; it understands your **intent**. It generates 3 distinct spiritual variations of your query to bridge the gap between modern language and ancient Sanskrit concepts.

### ✅ Path B: Self-Corrective Grading
To eliminate hallucinations, every retrieved verse is audited by a "Grader" LLM. If a verse isn't contextually relevant to your question, it's discarded before the final answer is written.

### 📜 Source Attribution
Every answer is cited. The system provides specific **Chapter and Verse** numbers so you can verify the wisdom directly in the scriptures.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit (Saffron & Gold Spiritual UI)
- **Backend:** FastAPI
- **Vector DB:** ChromaDB
- **Embeddings:** `all-MiniLM-L6-v2` (Running locally via HuggingFace)
- **Inference:** Llama-3.3-70B via **Groq** (Ultra-low latency)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- A [Groq API Key](https://console.groq.com/)
- Docker (Optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/hrithikumbarji/gitagpt.git](https://github.com/hrithikumbarji/gitagpt.git)
   cd gitagpt
