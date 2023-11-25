import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('flights.csv', sep=',').loc[:,['CARGO','PRICE','WEIGHT']]

fig, ax=plt.subplots()
aw = df.groupby('CARGO').sum()["WEIGHT"]
ap = df.groupby('CARGO').sum()["PRICE"]
ac = df.groupby('CARGO').count()["WEIGHT"]

ax = aw.plot(kind='bar')
ax.set_title("Weight per company")
plt.show()

fig, ax=plt.subplots()
ax = ap.plot(kind='bar')
ax.set_title("Price per company")
plt.show()

fig, ax=plt.subplots()
ax.set_title("Count per company")
ax = ac.plot(kind='bar')
plt.show()