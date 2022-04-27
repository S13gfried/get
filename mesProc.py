import numpy as np
import matplotlib.pyplot as plt

with open("settings.txt", "r") as specs:
    settings = [float(i) for i in specs.read().split("\n")]
    settings = np.array(settings)
    specs.close()
with open("data.txt", "r") as data:
    values = [float(i) for i in data.read().split("\n")]
    values = np.array(values)
    data.close()

maximumTime = np.argmax(values)/np.size(values)*settings[0]

#data = np.loadtxt("data.txt", dtype = int)
timing = np.linspace(0.0, settings[0], np.size(values))
#subTiming = 

figure, axes = plt.subplots(figsize=(9, 5), dpi = 300)

axes.margins(0.0, 0.0)

figure.suptitle("ЗАВИСИМОСТЬ НАПРЯЖЕНИЯ ОТ ВРЕМЕНИ", fontweight = "bold", fontsize = 20, wrap = True)

axes.set_title("Последовательная зарядка и разрядка конденсатора в RC-цепи", fontsize = 10, wrap = True)
axes.set_xlabel("Время с начала эксперимента [с]")
axes.set_ylabel("Напряжение на обкладках конденсатора [В]")

maxTicksY = int(values.max()/0.5) + 2
maxTicksX = int(settings[0]/10) + 1

axes.set_xlim(0, maxTicksX*10)
axes.set_ylim(0, maxTicksY*0.5)

major_ticks_top = np.linspace(0, maxTicksY*0.5, maxTicksY + 1)
minor_ticks_top = np.linspace(0, maxTicksY*0.5, maxTicksY*5 + 1)

major_ticks_bottom = np.linspace(0, maxTicksX*10, maxTicksX + 1)
minor_ticks_bottom = np.linspace(0, maxTicksX*10, maxTicksX*2 + 1)

axes.set_yticks(major_ticks_top)
axes.set_xticks(major_ticks_bottom)
axes.set_yticks(minor_ticks_top,minor=True)
axes.set_xticks(minor_ticks_bottom,minor=True)
axes.grid(which="major",alpha=0.8)
axes.grid(which="minor",alpha=0.8, linestyle = "--")

axes.text (1, maxTicksY*0.5-0.15, "ВРЕМЯ ЗАРЯДКИ: {:.2f} с".format(maximumTime), fontsize = 9, fontweight = "bold")
axes.text (1, maxTicksY*0.5-0.30, "ВРЕМЯ PAЗРЯДКИ: {:.2f} с".format(settings[0]-maximumTime), fontsize = 9, fontweight = "bold")

markers_on = np.arange(0, np.size(values), int(5/settings[0]*np.size(values)))

axes.plot(list(timing), list(values), markevery=markers_on, marker = "D", color = "red",  label = "V(t)", markersize = 6, linewidth = 1, mfc = "r", mec = "w")
axes.legend()

figure.savefig("plot.svg")
figure.savefig("plot.png")
#plt.show()