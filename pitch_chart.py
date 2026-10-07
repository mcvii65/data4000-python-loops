"""Startup Pitch Deck Visualizer"""

initial_revenue = float(input("Enter the initial revenue: "))
growth_rate = float(input("Enter the annual growth rate (%): "))

growth_rate_decimal = growth_rate / 100

print("Projected Revenue by Year")
for year in range(1, 11):
    projected_revenue = initial_revenue * ((1 + growth_rate_decimal) ** year)
    bar_length = max(1, int(projected_revenue / 1000))
    print(f"Year {year}: {'#' * bar_length}")
