#Print all student records
students = (
    ("Rajan", 22, "Nagpur", 85),
    ("Amit", 21, "Pune", 78),
    ("Priya", 23, "Mumbai", 92),
    ("Neha", 22, "Delhi", 67)
)
print("Student Records:")
for s in students:
    print("Name:", s[0], "| Age:", s[1], "| City:", s[2], "| Marks:", s[3])