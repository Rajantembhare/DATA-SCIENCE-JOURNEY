import pandas as pd

data = {
    "Name": ["Rajan", "Amit", "Sneha", "Priya"],
    "Age": [21, 25, 23, 22],
    "City": ["Nagpur", "Pune", "Mumbai", "Delhi"]
}
df = pd.DataFrame(data)

print(df.iloc[0])      # First row
print(df.iloc[1:3])      # Rows 2 to 3
print(df.iloc[:, 1]) # Entire 2nd column (Age)
print(df.iloc[0, 2])   # First row, 3rd column (City)