from datasets import load_dataset
from tqdm import tqdm
import json
import os

os.makedirs("data", exist_ok=True)
print("Downloading dataset ......")

dataset = load_dataset("JDhruv14/Bhagavad-Gita-QA","English", split="train")

print("Dataset downloaded")
print("Total datasets:", len(dataset))

docs = []
for row in tqdm(dataset):
    question = row.get("question", "")
    answer = row.get("answer","")
    combined_content = f"Question: {question}\nAnswer: {answer}"
    docs.append({
        "text": combined_content,
        "file": "Bhagavad-Gita-QA"  # The CSV doesn't have a 'file_name' column
    })

with open("data/raw.json", "w", encoding="utf-8") as f:
    json.dump(docs, f, ensure_ascii=False, indent=2)

print("✅ Dataset downloaded and saved to data/raw.json")
