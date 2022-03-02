import RPi.GPIO as io
import time
import math

leds = [24, 25, 8, 7, 12, 16, 20, 21]
lcount = len(leds)
aux = [2, 3, 14, 15, 18, 27, 23, 22]

io.cleanup()
io.setmode(io.BCM)

io.setup(leds, io.OUT)
io.setup(aux, io.IN)

while True:
    for i in range(lcount):
        io.output(leds[i], io.input(aux[i]))
