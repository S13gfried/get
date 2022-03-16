import RPi.GPIO as io
import time
import math

DACbits = [26, 19, 13, 6, 5, 11, 9, 10]
size = len(DACbits)
base = 2 ** size
basicVoltage = 3.3

period = 1 #seconds
tick = period/base

io.setmode(io.BCM)
io.setup(DACbits, io.OUT)

def dec2bin(source, length = 8):
    return  [int(bit) for bit in (bin(source)[2:])[-8:].zfill(length)]

try:
    while True:
        for level in range(base):
            io.output(DACbits, dec2bin(level, size))
            time.sleep(tick)
finally:
    io.output(DACbits, [0] * size)
    io.cleanup()

