"""Market Survey Analyzer"""

preferences = ["coffee", "tea", "coffee", "soda", "coffee", "tea", "soda", "coffee"]

counts = {}
for item in preferences:
    counts[item] = counts.get(item, 0) + 1

print("Market Survey Summary")
total_responses = sum(counts.values())

for product, count in counts.items():
    percent = (count / total_responses) * 100 if total_responses else 0
    print(f"{product}: {percent:.0f}%")
