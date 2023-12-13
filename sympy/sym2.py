import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
data=np.loadtxt('1.txt', skiprows=1)
A=data[:-1]
b=data[-1]
x=linalg.solve(A,b)
fig, ax=plt.subplots()
ax.grid()
ax.bar(range(len(x)),x)
plt.savefig('test.png')
