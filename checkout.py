"""Retail Checkout Simulation"""

prices = []

while True:
    user_input = input("Enter an item price (type 0 to finish): ")

    try:
        price = float(user_input)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if price < 0:
        print("Price cannot be negative. Please try again.")
        continue

    if price == 0:
        break

    prices.append(price)

if not prices:
    print("No items were purchased.")
else:
    total = sum(prices)
    average = total / len(prices)

    print("\nCheckout Summary")
    print(f"Total purchase amount: ${total:.2f}")
    print(f"Average item cost: ${average:.2f}")
    print(f"Number of items bought: {len(prices)}")
