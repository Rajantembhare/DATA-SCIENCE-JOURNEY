# to print the number of rows and columns by df.shape()
import pandas as pd
data={
    "NAME":["BMW","SUPRA","TATA","PHANTOM","TOYOTO","SUZUKI","VERNA","NEXON","SAFARI","THAR"],
    "PRIZE":["1CR","1CR","15LAKH","5CR","12LAKH","10LAKH","14LAKH","15LAKH","25LAKH","20LAKH"],
    "SPEED":["300KM","250KM","150KM","180KM","150KM","130KM","140KM","160KM","180KM","190KM"]
}
df=pd.DataFrame(data)
print(df)
print(df.shape)