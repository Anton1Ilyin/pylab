import matplotlib.pyplot as plt
import numpy as np

name="students.csv"
with open(name, 'r') as f:
    lines=f.readlines()
    a=[]
    groups=set()
    preps=set()
    for line in lines:
        s=line.split()
        a.append(s)
        preps.add(s[0])
        groups.add(s[1])
    weight_counts = {
        "Below": np.array([70, 31, 58]),
        "Above": np.array([82, 37, 66]),
    }
    for m in a:

    marksp={
        "1": np.array(),"2": np.array(),"3": np.array(),"4": np.array(),"5": np.array(),
        "6": np.array(),"7": np.array(),"8": np.array(),"9": np.array(),"10": np.array()
    }
    marksg = {
        "1": np.array(),"2": np.array(),"3": np.array(),"4": np.array(),"5": np.array(),
        "6": np.array(),"7": np.array(),"8": np.array(),"9": np.array(),"10": np.array()
    }
    width = 0.5

    fig, ax = plt.subplots()
    bottom = np.zeros(3)

    for boolean, weight_count in weight_counts.items():
        p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
        bottom += weight_count

    ax.set_title("Marks per prep")
    ax.legend(loc="upper right")

    plt.show()