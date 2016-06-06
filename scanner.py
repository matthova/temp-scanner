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
            logging.info(line)
        else:
            line = ser.readline()   # read a '\n' terminated line
            if line == 'echo:  M200 D0\n':
                logging.info('Serial port opened')
                opening = False
