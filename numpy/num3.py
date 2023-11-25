import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

u=np.loadtxt('np3.txt')
A=-1*np.eye(len(u), k=-1, dtype=int)+np.eye(len(u), dtype=int)
A[0][len(u)-1]=-1
u1 = np.zeros_like(u)

fig, ax = plt.subplots()
xdata, ydata = np.linspace(1, len(u), len(u)), u
ln, = ax.plot(xdata, ydata)

def init():
    return ln,

def update(frame):
    global ydata
    np.matmul(ydata, A.T, out=u1)
    ydata = ydata - 0.5 * u1
    if frame==254:
        ydata=u
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update,frames=255,init_func=init, blit=True, interval=20)
plt.show()