from mimetypes import init
import re
from weakref import ref
import RPi.GPIO as io
import time
import math

dacPins = [26, 19, 13, 6, 5, 11, 9, 10]
comparatorPin = 4
analogPowerPin = 17
indicator = [21, 20, 16, 12, 7, 8, 25, 24]

io.setmode(io.BCM)

io.setup(dacPins, io.OUT)
io.setup(indicator, io.OUT)
io.setup(analogPowerPin, io.OUT, initial = 1)
io.setup(comparatorPin, io.IN)

def dec2bin(source, length = 8):
    return  [int(bit) for bit in (bin(source)[2:])[-8:].zfill(length)]

def bin2decNormalized(source):
    scale = 1
    sum = 0
    for digit in source:
        sum = (sum * 2 + digit)
        scale *= 2
    return sum/scale

def dacWrite(dacPins, value):
    vector = dec2bin(value, len(dacPins))
    io.output(dacPins, vector)

def voltageBinarySearch(comp, pins):
    digits = len(pins)
    scale = int(2**(digits - 1))
    reference = scale - 1 #!

    vector = []

    for i in range(digits):
        dacWrite(dacPins, reference)
        time.sleep(0.0001)
        scale = int(scale / 2)
        if io.input(comparatorPin) == 0:
            vector.append(0)
            reference -= scale
        else:
            vector.append(1)
            reference += scale
    return vector


def bruteSearch(comp, pins):
    scale = 2**len(pins)
    for value in range(scale):
        dacWrite(dacPins, value)
        time.sleep(0.0001)
        if io.input(comp) == 0:
            return value

def healthbar(leds, value):
    size = len(leds)
    thres = (size+1)*value
    for i in range(size):
        if thres >= i + 1:
            io.output(leds[i], 1) 
        else:
            io.output(leds[i], 0) 
        

try:
    while True:
        #bruteSearch(comparatorPin, dacPins)
        vec = voltageBinarySearch(comparatorPin, dacPins)
        value = bin2decNormalized(vec)
        healthbar(indicator, value)
        print("{:.3f}".format(value * 3.3) + " VOLTS")
        time.sleep(0.02)
finally:
    io.cleanup()   