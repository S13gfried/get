import RPi.GPIO as io
print("frog")
io.setmode(io.BCM)

io.setup(14, io.OUT)
io.setup(15, io.IN)

while(True):
    io.output(14, io.input(15))