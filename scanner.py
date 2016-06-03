from time import sleep
import serial

opening = True
f = open('test.txt', 'ab+')

with serial.Serial('/dev/ttyACM0', 115200, timeout=1) as ser:
    while True:
	if opening == False:
	    ser.write('M105\n')
            sleep(1)
            line = ser.readline()
            f.write(line)
	else:
            line = ser.readline()   # read a '\n' terminated line
	    if line == 'echo:  M200 D0\n':
                print 'done opening'
                opening = False

