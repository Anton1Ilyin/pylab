import numpy as np
import matplotlib.pyplot as plt

a=np.loadtxt('signal03.dat')


b=np.cumsum(a)
d=np.zeros_like(a)
d[10:]=np.cumsum(a[:-10])
b-=d
b[10:]=b[10:]/10
b[:10]=b[:10]/np.linspace(1,10,10)


fig, ax = plt.subplots(nrows=1, ncols=2)

ax[1].plot(b)
ax[0].plot(a)
for w in ax:
    w.grid()
ax[1].set_title("With filter")
ax[0].set_title("No filter")
plt.savefig("signal03.png")
