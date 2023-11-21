import pandas as pd

df=pd.read_csv('transactions.csv', sep=',').loc[:,['CONTRACTOR','STATUS','SUM']]
print(df)
print("Task №1")
print(df[df['STATUS']=='OK'].sort_values(by='SUM', ascending=False).head(3))
print("Task №2")
real=df[df['STATUS']=='OK']
umb=real[real['CONTRACTOR']=='Umbrella, Inc'].loc[:,"SUM"].sum()
print(umb)