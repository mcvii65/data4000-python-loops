"""Business Growth Projection"""

initial_revenue = float(input("Enter the initial revenue: "))
growth_rate = float(input("Enter the annual growth rate (%): "))

growth_rate_decimal = growth_rate / 100

print("\nRevenue Growth Projection")
print(f"{'Year':<5} {'Revenue':>15}")

for year in range(1, 11):
    projected_revenue = initial_revenue * ((1 + growth_rate_decimal) ** year)
    print(f"{year:<5} ${projected_revenue:>13,.2f}")
