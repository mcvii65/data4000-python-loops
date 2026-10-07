"""Expense Report Categorizer"""

expenses = {
    "Travel": [500, 200],
    "Meals": [40, 60, 30],
    "Supplies": [100]
}

grand_total = 0
print("Expense Summary Report")
print("-" * 25)

for category, amounts in expenses.items():
    category_total = 0

    for amount in amounts:
        category_total += amount
        grand_total += amount

    print(f"{category:<8}: ${category_total:>7.2f}")

print("-" * 25)
print(f"Grand total: ${grand_total:.2f}")
