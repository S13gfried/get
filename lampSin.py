import RPi.GPIO as io
import time
import math

bits = [10, 9, 11, 5, 6, 13, 19, 26, 24, 25, 8, 7, 12, 16, 20, 21]

totalTime = 60
frequency = 4
ticks = totalTime * frequency

def int2bool(source, length = 8):

    key = []
    intSrc = int(source)

    for i in range(length):
        key.append(intSrc % 2)
        intSrc = intSrc // 2

    return key

io.setmode(io.BCM)

io.setup(bits, io.OUT)

while True:
    io.output(bits, int2bool(int(input()), len(bits)))