import pandas as pd
result={
    "result":["pass","fail","moderate"],
    "date":["24","56","54"],
    "college":["jd","jit","nit"],
    "job":["it","finance","hr"],
    
}
df=pd.DataFrame(result)
print(df)