import json
import shutil
import hashlib
from pathlib import Path
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "gita_collection"
RESET_DB = True
BATCH_SIZE = 200

#Reset
if RESET_DB and Path(CHROMA_DIR).exists():
    print("🧹 Removing existing Chroma DB...")
    shutil.rmtree(CHROMA_DIR)

#Load Chunks

print("📂 Loading chunks...")
with open("data/chunk_dataset.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

total_chunks = len(chunks)
print(f"✅ Loaded {total_chunks} chunks")

if total_chunks == 0:
    raise ValueError("No chunks found. Aborting.")

#Load Embedding Model

print("🧠 Loading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "mps"},
    encode_kwargs={"normalize_embeddings": True}
)

print("✅ Embedding model ready on MPS (GPU)")

#Initialize Chroma

print("📦 Initializing Chroma vector store...")

db = Chroma(
    collection_name=COLLECTION_NAME,
    persist_directory=CHROMA_DIR,
    embedding_function=embeddings
)

#Helper: Stable ID Generator

def generate_id(text: str) -> str:
    """
    Generate deterministic ID based on content.
    Prevents duplicates across runs.
    """
    return hashlib.sha256(text.strip().lower().encode()).hexdigest()

#Batch Embedding
print(f"🚀 Starting embedding in batches of {BATCH_SIZE}")

for i in range(0, total_chunks, BATCH_SIZE):
    end = min(i + BATCH_SIZE, total_chunks)
    print(f"🔹 Processing {i + 1} → {end} / {total_chunks}")

    batch = chunks[i:end]

    texts = []
    metadatas = []
    ids = []

    for chunk in batch:
        text = chunk["text"].strip()
        metadata = chunk.get("metadata", {})

        if not text:
            continue

        texts.append(text)
        metadatas.append(metadata)
        ids.append(generate_id(text))

    if texts:
        db.add_texts(
            texts=texts,
            metadatas=metadatas,
            ids=ids
        )

#Persist DB

persist_directory="chroma_db"

print("\n🎉 Chroma embedding complete!")
print(f"📁 Vector DB saved at: {CHROMA_DIR}")