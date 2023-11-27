import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
with open('1.txt') as f:
    n=int(f.readline())
    A=np.zeros((n,n))
    for i in range(n):
        A[i,:]=np.array(f.readline().split(),dtype=np.float64)
    b=np.array(f.readline().split(),dtype=np.float64)
    x=linalg.solve(A,b)
    fig, ax=plt.subplots()
    ax.grid()
    ax.bar(range(len(x)),x)
    plt.savefig('test.png')
