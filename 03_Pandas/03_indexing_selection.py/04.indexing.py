import pandas as pd

data = {
    "Name": ["Rajan", "Amit", "Sneha", "Priya"],
    "Age": [21, 25, 23, 22],
    "City": ["Nagpur", "Pune", "Mumbai", "Delhi"]
}
df = pd.DataFrame(data)
print(df[df["Age"] > 22])       # Students older than 22
print(df[df["City"] == "Pune"]) # Students from Pune
