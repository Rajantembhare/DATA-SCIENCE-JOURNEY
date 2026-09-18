import pandas as pd

data = {
    "Name": ["Rajan", "Amit", "Sneha", "Priya"],
    "Age": [21, 25, 23, 22],
    "City": ["Nagpur", "Pune", "Mumbai", "Delhi"]
}
df = pd.DataFrame(data)

print(df["Name"])          # Single column
print(df[["Name", "City"]]) # Multiple columns
