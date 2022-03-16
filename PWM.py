import RPi.GPIO as io
import time
import math

DACbits = [26, 19, 13, 6, 5, 11, 9, 10]
size = len(DACbits)
base = 2 ** size
basicVoltage = 3.3

PWMpin = 18

period = 1 #seconds
tick = period/base

def dec2bin(source, length = 8):
    return  [int(bit) for bit in (bin(source)[2:])[-8:].zfill(length)]

io.setmode(io.BCM)
io.setup(DACbits, io.OUT)
io.setup(PWMpin, io.OUT) 

PWM = io.PWM(PWMpin, 50)
PWM.start(0)

try:
    while True:
        try:
            print("set PWM output:")
            value = int(input())
            PWM.ChangeDutyCycle(int(100*value/base))
            print("VOLTAGE SET TO {:.2f} V".format(value*3.3/base))
        except ValueError:
            print("Invalid input")
        
        #try:
        #    print("set DAC output:")
        #    value = int(input())
        #    io.output(DACbits, dec2bin(value, size))
        #except ValueError:
        #    print("Invalid input")

finally:
    io.output(DACbits, [0] * size)
    io.cleanup()

