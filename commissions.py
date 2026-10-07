"""Sales Commission Calculator"""


def calculate_commission(sales_amount):
    return sales_amount * 0.10


sales = {
    "Alice": 5000,
    "Bob": 7000,
    "Carol": 3000
}

leaderboard = []
for employee, total_sales in sales.items():
    leaderboard.append((employee, calculate_commission(total_sales)))

leaderboard.sort(key=lambda item: item[1], reverse=True)

print("Sales Commission Leaderboard")
print("-" * 30)
for rank, (employee, commission_amount) in enumerate(leaderboard, start=1):
    print(f"{rank}. {employee:<6} - ${commission_amount:,.2f}")
