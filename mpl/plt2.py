import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

name="2.txt"
with open(name, 'r') as f:
    lines=f.readlines()
    minx=min([min([float(z) for z in i.split()]) for i in lines[::2]])
    maxx=max([max([float(z) for z in i.split()]) for i in lines[::2]])
    miny=min([min([float(z) for z in i.split()]) for i in lines[1::2]])
    maxy=max([max([float(z) for z in i.split()]) for i in lines[1::2]])
    for j in range(0, len(lines), 2):
        fig, ax = plt.subplots()
        x=[float(i) for i in lines[j].split()]
        y=[float(i) for i in lines[j+1].split()]
        ax.plot(x,y)
        ax.set_xlim(left=minx, right=maxx)
        ax.set_ylim(bottom=miny-2, top=maxy+2)
        ax.grid(which='major', color='k')
        ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        plt.title("Frame"+str(j//2+1))
        plt.savefig("Frame"+str(j//2) + ".png")