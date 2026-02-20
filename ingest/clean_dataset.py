import json
import os
import re

# 1. Setup
os.makedirs("data", exist_ok=True)

def clean_text(text: str) -> str:
    """Removes extra whitespace and fixes formatting."""
    # Remove common CSV header artifact
    text = text.replace("filename,text", "")
    # Reduce 3+ newlines to 2, and multiple spaces to 1
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

# 2. Load the raw data
with open("data/raw.json", "r", encoding="utf-8") as f:
    rows = json.load(f)

docs = []

print(f"Processing {len(rows)} entries...")

for r in rows:
    raw_content = r.get("text", "")
    
    # 3. Split the text into Question and Answer
    # We use a case-insensitive regex split to catch 'Question:' or 'question:'
    parts = re.split(r'(?i)Question:|Answer:', raw_content)
    
    # parts[0] is usually empty (stuff before 'Question:')
    # parts[1] is the Question content
    # parts[2] is the Answer content
    if len(parts) >= 3:
        q_content = clean_text(parts[1])
        a_content = clean_text(parts[2])
        
        # We skip rows where either side is empty
        if q_content and a_content:
            # This is the 'RAG-Ready' structure
            docs.append({
                # 'text' is what the AI will read to generate its response
                "text": f"Question: {q_content}\nAnswer: {a_content}",
                # 'metadata' helps with search accuracy and filtering
                "metadata": {
                    "source_question": q_content
                }
            })

# 4. Save the result
output_file = "data/cleaned.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(docs, f, indent=2, ensure_ascii=False)

print(f"Cleanup finished! Created {len(docs)} clean documents.")