import RPi.GPIO as io
import time
import math

#bits = [10, 9, 11, 5, 6, 13, 19, 26] 
bits = [24, 25, 8, 7, 12, 16, 20, 21]

io.setmode(io.BCM)
io.setup(bits, io.OUT)

frequency = 1
seed = [0, 0, 0, 0, 0, 0, 0, 0]

while True:
    for i in range(len(bits)):

    time.sleep(1/frequency)