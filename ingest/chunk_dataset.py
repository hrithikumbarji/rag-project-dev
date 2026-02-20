import json
import hashlib
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Setup
os.makedirs("data", exist_ok=True)

# Load the cleaned data
with open("data/cleaned.json", "r", encoding="utf-8") as f:
    docs = json.load(f)

# 2. Configure Splitter
# We increase chunk_size slightly to 600 to try and keep most Q&A pairs whole.
# If a pair is longer than 600, it splits recursively on newlines or spaces.
splitter = RecursiveCharacterTextSplitter(
    chunk_size=600,
    chunk_overlap=100,
    separators=["\n\n", "\n", " ", ""]
)

def get_hash(text): 
    return hashlib.sha256(text.lower().encode()).hexdigest()

seen_hashes = set()
chunks = []

print(f"Chunking {len(docs)} documents...")

for d in docs:
    # Use the full text we built in the previous step
    content = d["text"]
    source_q = d["metadata"].get("source_question", "Unknown")
    
    # Split the text into smaller pieces
    parts = splitter.split_text(content)
    
    for i, p in enumerate(parts):
        text_hash = get_hash(p)
        
        # Deduplication check
        if text_hash in seen_hashes:
            continue
        seen_hashes.add(text_hash)
        
        chunks.append({
            "text": p,
            "metadata": {
                "source_question": source_q,
                "chunk_index": i,
                "total_chunks": len(parts)
            }
        })

# 3. Save the chunks
with open("data/chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, indent=2, ensure_ascii=False)

print(f"Success! Created {len(chunks)} chunks from {len(docs)} documents.")