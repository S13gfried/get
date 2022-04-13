import numpy as np
import matplotlib.pyplot as plt
import RPi.GPIO as io
import time
import math

dacPins = [26, 19, 13, 6, 5, 11, 9, 10]
comparatorPin = 4
analogPowerPin = 17
indicator = [21, 20, 16, 12, 7, 8, 25, 24]

measured_data = []

deltaTime = 0.1
deltaV = 3.3/(2**len(dacPins))
specs = [0, deltaV]

io.setmode(io.BCM)

io.setup(dacPins, io.OUT)
io.setup(analogPowerPin, io.OUT, initial = 1)
io.setup(indicator, io.OUT, initial = 0)
io.setup(comparatorPin, io.IN)

def getVoltage(comp, pins):

    size = len(pins)
    vector = [0]*size

    sum = 0

    for i in range(size):
        vector[i] = 1
        io.output(pins, vector)
        time.sleep(0.001)
        sum *= 2
        if (io.input(comp) == 0):
            vector[i] = 0 
        else:
            sum += 1

    return sum

def healthbar(leds, value):
    io.output(leds, 0)
    size = len(leds)
    thres = (size + 1)*value
    for i in range(size):
        if thres < i + 1:
            break
        io.output(leds[i], 1)

try:
    timer = 0
    peak = False
    while True:
        value = getVoltage(comparatorPin, dacPins)
        measured_data.append(value * deltaV)
        print(value)
        healthbar(indicator, value/256)
        timer += 1
        time.sleep(deltaTime)
        if value > 252:
            peak = True
            io.output(analogPowerPin, 0)
        if value < 4 and peak:
            break
    
    specs[0] = timer*deltaTime

    with open("data.txt", "w") as data:
        measured_data_str = [str(i) for i in measured_data]
        data.write("\n".join(measured_data_str))
    with open("settings.txt", "w") as data:
        specs_str = [str(i) for i in specs]
        data.write("\n".join(specs_str))
    figure, axes = plt.subplots(figsize = (4, 7), dpi = 300)
    axes.plot(measured_data)
    figure.savefig("graph.png")
    plt.show()

finally:
    io.cleanup() 

 
plt.plot(measured_data)
plt.show()