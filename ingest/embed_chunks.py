import json
import shutil
import os
from pathlib import Path
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

CHROMA_DIR = "chroma_db"

# 1. Reset Database
if Path(CHROMA_DIR).exists():
    print("🧹 Removing existing Chroma DB...")
    shutil.rmtree(CHROMA_DIR)

# 2. Load Chunks
print("📂 Loading chunks...")
with open("data/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

total_chunks = len(chunks)
print(f"✅ Loaded {total_chunks} chunks")

print("🧠 Loading embedding model...")
model_kwargs = {'device': 'mps'}
encode_kwargs = {'normalize_embeddings': True}

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)
print("✅ Embedding model ready on MPS (GPU)")

# 3. Initialize Chroma
print("📦 Initializing Chroma vector store...")
db = Chroma(
    collection_name="gita_collection",
    persist_directory=CHROMA_DIR,
    embedding_function=embeddings
)

# 4. Embed in Smaller Batches
BATCH = 200
print(f"🚀 Starting embedding in batches of {BATCH}")

for i in range(0, total_chunks, BATCH):
    end = min(i + BATCH, total_chunks)
    print(f"🔹 Processing {i + 1} → {end} / {total_chunks}")

    batch_chunks = chunks[i:end]
    
    # We pass the content ('text') and the metadata dict
    db.add_texts(
        texts=[c["text"] for c in batch_chunks],
        metadatas=[c["metadata"] for c in batch_chunks]
    )

print("\n🎉 Chroma embedding complete!")
print(f"📁 Vector DB saved at: {CHROMA_DIR}")