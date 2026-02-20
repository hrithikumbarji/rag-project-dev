import json
import hashlib
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

#Setup
os.makedirs("data", exist_ok=True)

with open("data/cleaned.json", "r", encoding="utf-8") as f:
    docs = json.load(f)

#splitter Configuration
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=120,
    separators=["\n\n", "\n", " ", ""]
)

def get_hash(text):
    return hashlib.sha256(text.lower().encode()).hexdigest()

seen_hashes = set()
chunks = []

print(f"Chunking {len(docs)} documents...")

for doc_id, d in enumerate(docs):

    content = d["text"]
    metadata = d.get("metadata", {})

    source_q = metadata.get("source_question", "Unknown")
    source_file = metadata.get("source_file", "Unknown")

    #If content is short, don't split unnecessarily
    if len(content) <= 800:
        parts = [content]
    else:
        parts = splitter.split_text(content)

    for i, part in enumerate(parts):
        cleaned_part = part.strip()
        if not cleaned_part:
            continue

        text_hash = get_hash(cleaned_part)
        if text_hash in seen_hashes:
            continue
        seen_hashes.add(text_hash)

        chunks.append({
            "text": cleaned_part,
            "metadata": {
                "doc_id": doc_id,
                "source_question": source_q,
                "source_file": source_file,
                "chunk_index": i,
                "total_chunks": len(parts),
                "type": "qa_explanation"
            }
        })

#Save the chunks

with open("data/chunk_dataset.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, indent=2, ensure_ascii=False)

print(f"Success! Created {len(chunks)} chunks from {len(docs)} documents.")