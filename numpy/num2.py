import numpy as np
import matplotlib.pyplot as plt

a=np.loadtxt('signal03.dat')
b=np.zeros_like(a)

for i in range(len(b)):
    b[i]=a[max(0,i-9):i+1].mean()
fig, ax = plt.subplots(nrows=1, ncols=2)

ax[1].plot(b)
ax[0].plot(a)
for w in ax:
    w.grid()
ax[1].set_title("With filter")
ax[0].set_title("No filter")
plt.savefig("signal03.png")
