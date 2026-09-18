import pandas as pd

data = {
    "Name": ["Rajan", "Amit", "Sneha", "Priya"],
    "Age": [21, 25, 23, 22],
    "City": ["Nagpur", "Pune", "Mumbai", "Delhi"]
}
df = pd.DataFrame(data)
print(df.loc[0])              # Row with index 0
print(df.loc[0, "City"])      # Specific cell (row 0, column "City")
print(df.loc[:, "Name"])      # Entire Name column
print(df.loc[0:2, ["Name","Age"]])  # Rows 0–2, only Name & Age