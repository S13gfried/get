import numpy as np
import matplotlib.pyplot as plt

with open("specs.txt", "r") as specs:
    vector = [float(i) for i in specs.read().split("\n")]

data = np.loadtxt("data.txt", dtype = int)

figure, axes = plt.subplots(figsize=(4, 7), dpi = 300)

axes.plot(data)
figure.savefig("plot.png")
plt.show()