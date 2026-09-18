import pandas as pd
marks={
    "Name":["Rajan","Anugra","Shruti","Rohan"],
    "Dept":["finance","IT","Bio","Security"],
    "salary":["10000000","25435","2500000","486951"],
    "address":["kuwait","india","russia","germany"]
    
    
}
df=pd.DataFrame(marks)
print(df)
print(df["salary"])
