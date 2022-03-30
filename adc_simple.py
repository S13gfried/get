from mimetypes import init
import RPi.GPIO as io

dacPins = [26, 19, 13, 6, 5, 11, 9, 10]
comparatorPin = 4
analogPowerPin = 17

io.setmode(io.BCM)

io.setup(dacPins, io.OUT)
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

def bruteSearch(comp, pins):
    scale = 2**len(pins)
    for value in range(scale):
        dacWrite(dacPins, value)
        if io.input(comp) == 0:
            return value


try:
    while True:
        bruteSearch(comparatorPin, dacPins)
finally:
    io.cleanup()   