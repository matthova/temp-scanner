import logging
import serial
from time import sleep

opening = True

logging.basicConfig(filename='temp.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

with serial.Serial('/dev/ttyACM0', 115200, timeout=1) as ser:
    while True:
    if opening == False:
        ser.write('M105\n')
        sleep(1)
        line = ser.readline()
        f.write(line)
        logging.info(line)
    else:
        line = ser.readline()   # read a '\n' terminated line
        if line == 'echo:  M200 D0\n':
            print 'done opening'
            opening = False
