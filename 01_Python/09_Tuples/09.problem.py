# Each tuple = (Date, Location, Number_of_Chicken_Sold, Price_per_Chicken)
sales = (
    ("2026-10-01", "Nagpur", 120, 150),
    ("2026-10-02", "Bhandara", 90, 145),
    ("2026-10-03", "Gondia", 110, 148),
    ("2026-10-04", "Nagpur", 130, 150),
)

# 1. Print all sales records
print("Daily Sales Records:")
for record in sales:
    print("Date:", record[0], "| Location:", record[1],
          "| Chickens Sold:", record[2], "| Price:", record[3])

# 2. Calculate total chickens sold
total_chickens = sum(r[2] for r in sales)
print("\nTotal Chickens Sold:", total_chickens)

# 3. Calculate total revenue
total_revenue = sum(r[2] * r[3] for r in sales)
print("Total Revenue (₹):", total_revenue)

# 4. Find the best sales day (max chickens sold)
best_day = max(sales, key=lambda x: x[2])
print("Best Sales Day:", best_day[0], "at", best_day[1], "with", best_day[2], "chickens")

# 5. Average price per chicken across days
avg_price = sum(r[3] for r in sales) / len(sales)
print("Average Price per Chicken:", avg_price)
