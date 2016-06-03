from time import sleep
import serial

opened = False

with serial.Serial('/dev/ttyACM0', 115200, timeout=1) as ser:
    while True:
	if opened == True:
	    ser.write('M105\n')
            sleep(1)
            line = ser.readline()
            with open('test.txt', 'a') as f:
                print line
                f.write(line)
	else:
            line = ser.readline()   # read a '\n' terminated line
	    if line == 'echo:  M200 D0\n':
                print 'done opening'
                opened = True

