import matplotlib.pyplot as plt

for i in range(5):
    name="00"+str(i+1)+".dat"
    with open(name, 'r') as f:
        x=[]
        y=[]
        for j in range(int(f.readline())):
            a,b=(float(z) for z in f.readline().split())
            x.append(a)
            y.append(b)
        plt.scatter(x,y)
        plt.title(name)
        plt.savefig(name+".png")