"""
Drives RoboClaw 2x15A Moter Driver

Setup:

Set RoboClaw in Mode 5: standar serial
   - Press MODE -> Press set to increase, Press MODE to decrease -> Press LIPO to save
Set RoboClaw in Option 2: 9600 baud rate
   - Press SET -> Press set to increase, Press MODE to decrease -> Press LIPO to save
"""

from time import sleep
import serial
import curses


screen = curses.initscr()
curses.cbreak()
screen.keypad(1)
screen.nodelay(True)
key = ''


def serialWrite(port, values = [64, 192]):
    print "%d  %d" % (values[0], values[1])
    string = ''.join(chr(character) for character in values)
    port.write(string)


serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
#        
speed = [64, 192]

while key != ord('q'):
    key = screen.getch()
    screen.refresh()

    pressed = False
    if key != curses.ERR:
        pressed = True
        if key == curses.KEY_UP:
            #screen.addstr(0, 0, "Up")
            if speed[0] < 84:
                speed[0] = speed[0] + 5
            if speed[1] < 212: 
                speed[1] = speed[1] + 5
    
        elif key == curses.KEY_DOWN:
            #screen.addstr(0, 0, "Down")
            if speed[0] > 45:
                speed[0] = speed[0] - 5
            if speed[1] > 172:
                speed[1] = speed[1] - 5
    
        elif key == curses.KEY_LEFT:
            #screen.addstr(0, 0, "Left")
            if speed[0] < 84:
                speed[0] = speed[0] + 5
            if speed[1] > 172:
                speed[1] = speed[1] - 5
 
        elif key == curses.KEY_RIGHT:
            #screen.addstr(0, 0, "Right")
            if speed[0] > 45:
                speed[0] = speed[0] - 5
            if speed[1] < 212:
                speed[1] = speed[1] + 5


    serialWrite(serialport, speed)
    screen.addstr(0, 0, '{} {}'.format(speed[0], speed[1]))
    if not pressed:
        sleep(0.5)
        if speed[0] - 64 > 0:
            speed[0] = speed[0] - 10
            if speed[0] < 64:
                speed[0] = 64
        else:
            speed[0] = speed[0] + 10
            if speed[0] > 64:
                speed[0] = 64

        if speed[1] - 192 > 0:
            speed[1] = speed[1] - 10
            if speed[1] < 192:
                speed[1] = 192
        else:
            speed[1] = speed[1] + 10
            if speed[1] > 192:
                speed[1] = 192


serialport.close()
curses.endwin()

