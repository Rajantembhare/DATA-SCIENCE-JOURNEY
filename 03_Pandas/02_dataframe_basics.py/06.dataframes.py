#we can use the df.tail() to print the last five rows

import pandas as pd
data={
    "college":["jit","nit","raisoni","Tgp","IIT","JD"],
    "branch":["AI-ML","DATASCIENCE","IT","ECE","MECHANICAL","ELECTRICAL"],
    "PACKAGE":["10LPA","12LPA","15LPA","9LPA","50LPA","5LPA"],
    "CAMPUS":["5ACRE","15ACRE","20ACRE","6ACRE","50ACRE","12ACRE"],
    "FACULTY":["GOOD","BEST","BEST","GOOD","BEST","BEST"],
    "COMPANY":["TECHMAHENDRA","MICROSOFT","IBM","BMW","FINTECH","GOOGLE"],
    "EVENT":["JALLOSH","PKALPA","ALPHA","SIKHAR","TECHARENA","SAFAR"]
    
} 
df=pd.DataFrame(data)
print(df)
print(df.tail())