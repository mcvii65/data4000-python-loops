"""Stock Portfolio Tracker"""

import random

portfolio = {
    "AAPL": {"shares": 10, "price": 170},
    "TSLA": {"shares": 4, "price": 250},
    "AMZN": {"shares": 2, "price": 130}
}


def total_portfolio_value(portfolio_dict):
    total = 0
    for stock, info in portfolio_dict.items():
        total += info["shares"] * info["price"]
    return total

print("Current Portfolio Value")
print(f"Total value: ${total_portfolio_value(portfolio):,.2f}")

print("\nSimulated weekly price changes:")
for day in range(1, 6):
    for stock, info in portfolio.items():
        change_percent = random.uniform(-0.05, 0.05)
        info["price"] = round(info["price"] * (1 + change_percent), 2)

    value = total_portfolio_value(portfolio)
    print(f"Day {day}: ${value:,.2f}")
