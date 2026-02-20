import json
import os
import re

os.makedirs("data", exist_ok=True)

def clean_text(text: str) -> str:
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

with open("data/raw.json", "r", encoding="utf-8") as f:
    rows = json.load(f)

docs = []

print(f"Processing {len(rows)} entries...")

for r in rows:
    raw_content = r.get("text", "")
    source_file = r.get("file", "unknown")

    # Split Question / Answer
    parts = re.split(r'(?i)Question:|Answer:', raw_content)

    if len(parts) >= 3:
        question = clean_text(parts[1])
        answer = clean_text(parts[2])

        if question and answer:
            docs.append({
                # Only embed the answer
                "text": answer,
                "metadata": {
                    "source_question": question,
                    "source_file": source_file,
                    "type": "qa_explanation"
                }
            })

output_file = "data/cleaned.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(docs, f, indent=2, ensure_ascii=False)

print(f"Cleanup finished! Created {len(docs)} clean QA documents.")