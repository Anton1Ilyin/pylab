import pandas as pd

s=set()
df=pd.read_csv('flights.csv', sep=',').loc[:,['CARGO','PRICE','WEIGHT']]
print(df)
for i in df.loc[:, 'CARGO']:
    s.add(i)
data2=[]
for i in s:
    w=df[df["CARGO"]==i].loc[:,"WEIGHT"].sum()
    p=df[df["CARGO"]==i].loc[:,"PRICE"].sum()
    k=len(df[df["CARGO"]==i].loc[:,"WEIGHT"])
    data2.append((i,w,p,k))
print(pd.DataFrame(data2,columns=("CARGO", "WEIGHT","PRICE","COUNT")))
