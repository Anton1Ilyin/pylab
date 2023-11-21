import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

u=np.loadtxt('np3.txt')
A=np.zeros((len(u),len(u)))
A[0][len(u)-1]=-1
for i in range(len(u)):
    A[i][max(0,i-1)]=-1
    A[i][i]=1
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