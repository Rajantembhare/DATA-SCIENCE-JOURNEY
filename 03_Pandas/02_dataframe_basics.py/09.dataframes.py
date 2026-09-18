# Data types of each column
import pandas as pd
data={
    "name":["Rajan","Anil","kailsh","sneha","soham"],
    "job":["Finance","Security","IT","R&D","teaching"]
}

df=pd.DataFrame(data)
print(df)
print(df.dtypes)