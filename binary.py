import RPi.GPIO as io
import time
import math

DACbits = [26, 19, 13, 6, 5, 11, 9, 10]
size = len(DACbits)
base = 2 ** size
basicVoltage = 3.3

io.setmode(io.BCM)
io.setup(DACbits, io.OUT)

def dec2bin(source, length = 8):
    return  [int(bit) for bit in (bin(source)[2:])[-8:].zfill(length)]

while True:
    inbox = input()
    if inbox == "q":
        break

    try: 
        val = float(inbox)

        if val % 1 != 0:
            print("The function does not take non-integer values; Please try again.")
            continue

        val = int(val)

        if val > 255:
            print("Value out of range; Please try again.")
            continue

        if val < 0:
            print("The function does not take negative values; Please try again.")
            continue

        io.output(DACbits, dec2bin(val, size))
        print("VOLTAGE: {:.2f} V".format(float(val)*basicVoltage/base))

    except ValueError:
        print("invalid user input; Please try again.")
    except KeyboardInterrupt:
        break

io.output(DACbits, [0] * size)
io.cleanup()

