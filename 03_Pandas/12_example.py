import pandas as pd
# Load data
df = pd.read_csv('employees.csv')
# Understand data
print(df.head())
print(df.shape)
print(df.info())
# Remove duplicate rows
df = df.drop_duplicates()
# Convert Salary to numeric
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
# Fill missing Salary with median
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
# Select high-salary employees
high_salary = df[df['Salary'] > 50000]
# Average salary by department
summary = df.groupby('Department')['Salary'].mean()
# Save result
high_salary.to_csv('high_salary.csv', index=False)