# the code of dataframes to form the data in coloumn in rows


import pandas  as pd
  
data = {
'Name': ['Ravi', 'Asha', 'Neha'],
'Marks': [78, 92, 85],
'City': ['Nagpur', 'Pune', 'Mumbai']
}
df = pd.DataFrame(data)
print(df)
