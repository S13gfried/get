import RPi.GPIO as io
import time

bits = [24, 25, 8, 7, 12, 16, 20, 21]

totalTime = 10
cycles = 6
leds = 8

ticks = cycles*leds

io.setmode(io.BCM)
io.setup(bits, io.OUT)

for i in range(ticks):
    
    io.output(bits[(i - 1)%leds], 0)
    io.output(bits[i%leds], 1)
    time.sleep(totalTime/ticks)
