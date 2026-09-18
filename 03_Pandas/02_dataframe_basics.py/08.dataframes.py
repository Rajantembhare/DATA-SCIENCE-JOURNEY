import pandas as pd
data={
    "city":["nagpur","bhandara","pune","mumbai","bhopal","akola"],
    "count":["10lakh","5lakh","19lakh","99lakh","25lakh","15lakh"],
    "cars":["20lakh","25lakh","30lakh","1cr","20lakh","15lakh"]
}
df=pd.DataFrame(data)
print(df)
print(df.columns)
