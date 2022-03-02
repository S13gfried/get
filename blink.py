import RPi.GPIO as io
import time

io.setmode(io.BCM)

io.setup(14, io.OUT)

for i in range(10):
    io.output(14, i%2)
    time.sleep(1)
