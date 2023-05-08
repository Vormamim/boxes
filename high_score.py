import json

high_scores = {
    "Alice": 100,
    "Bob": 80,
    "Charlie": 120,
    "David": 90
}

with open("high_scores.json", "w") as f:
    json.dump(high_scores, f)
    
with open("high_scores.json", "r") as f:
    high_scores = json.load(f)

for name, score in high_scores.items():
    print(f"{name}: {score}")
