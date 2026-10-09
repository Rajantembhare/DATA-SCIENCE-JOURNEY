# Each tuple = (Ticket_ID, Passenger_Name, Source, Destination, Fare)
tickets = (
    (101, "Rajan", "Nagpur", "Pune", 750),
    (102, "Amit", "Bhandara", "Nagpur", 250),
    (103, "Priya", "Nagpur", "Mumbai", 1200),
    (104, "Neha", "Gondia", "Nagpur", 300),
)

# 1. Print all ticket records
print("Bus Ticket Records:")
for t in tickets:
    print("Ticket:", t[0], "| Name:", t[1], "| From:", t[2], "| To:", t[3], "| Fare: ₹", t[4])

# 2. Calculate total revenue
total_revenue = sum(t[4] for t in tickets)
print("\nTotal Revenue (₹):", total_revenue)

# 3. Find the highest fare ticket
highest_fare = max(tickets, key=lambda x: x[4])
print("Highest Fare Ticket:", highest_fare)

# 4. Count how many passengers are traveling from Nagpur
nagpur_count = sum(1 for t in tickets if t[2] == "Nagpur")
print("Passengers starting from Nagpur:", nagpur_count)

# 5. Tuple unpacking example
print("\nUnpacking Example:")
ticket_id, name, source, destination, fare = tickets[0]
print("First Ticket →", ticket_id, name, source, destination, fare)

# 6. Membership check
print("\nIs 'Mumbai' a destination?", any(t[3] == "Mumbai" for t in tickets))

# 7. Average fare calculation
avg_fare = sum(t[4] for t in tickets) / len(tickets)
print("Average Fare:", avg_fare)

# 8. Using tuple as dictionary key (route mapping)
routes = {
    ("Nagpur", "Pune"): "Express Bus",
    ("Nagpur", "Mumbai"): "Luxury Bus",
    ("Bhandara", "Nagpur"): "Local Bus"
}
print("Route Nagpur → Mumbai:", routes[("Nagpur", "Mumbai")])
