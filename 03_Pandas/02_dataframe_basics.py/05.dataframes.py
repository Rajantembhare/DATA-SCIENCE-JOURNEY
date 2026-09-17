import pandas    as pd
data={
    "Name":["rajan","anugra","anmol","anurag"],
    "Marks":["99","87","79","52"],
    "Result":["Pass","Pass","Pass","Fail"],
    "carrier":["finance","HR","Manager","Businessman"],
    "Location":["Germany","India","Canada","Qatar"]
    
    
}
df=pd.DataFrame(data)
print(df)