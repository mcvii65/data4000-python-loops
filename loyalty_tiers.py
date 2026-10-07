"""Customer Loyalty Tiers"""

customers = {
    "Ava": 800,
    "Ben": 1500,
    "Cara": 4200,
    "Damon": 6000,
    "Ella": 5000
}

tier_counts = {
    "Bronze": 0,
    "Silver": 0,
    "Gold": 0
}

for customer, total_spent in customers.items():
    if total_spent < 1000:
        tier = "Bronze"
    elif total_spent < 5000:
        tier = "Silver"
    else:
        tier = "Gold"

    tier_counts[tier] += 1
    print(f"{customer}: {tier}")

print("\nTier Summary")
for tier, count in tier_counts.items():
    print(f"{tier}: {count}")
