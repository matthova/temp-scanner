import logging
import serial
from time import sleep

# Create logging file
logging.basicConfig(filename='/home/pi/temp-scanner/temp.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

# Global boolean for if the serial port is open
serial_is_open = False

with serial.Serial('/dev/ttyACM0', 115200, timeout=1) as ser:
    while True:
        if serial_is_open:
            ser.write('M105\n')
            sleep(1)
            line = ser.readline()
            logging.info(line)
        else:
            line = ser.readline()   # read a '\n' terminated line
            if line == 'echo:  M200 D0\n':
                logging.info('Serial port opened')
                serial_is_open = True
