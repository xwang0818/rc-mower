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
speed = [64, 192]

# for i in range(1, 63):
#    speed[0] = speed[0] + 1
#    speed[1] = speed[1] + 1
#    serialWrite(serialport, speed)
#    sleep(0.5)

#speed = [127, 255]
#for i in range(1, 63):
#    speed[0] = speed[0] - 1
#    speed[1] = speed[1] - 1
#    serialWrite(serialport, speed)
#    sleep(0.5)


while key != ord('q'):
    key = screen.getch()
    screen.refresh()

    pressed = False
    if key != curses.ERR:
        pressed = True
        if key == curses.KEY_UP:
            #screen.addstr(0, 0, "Up")
            if speed[0] < 94:
                speed[0] = speed[0] + 5
            if speed[1] < 212: 
                speed[1] = speed[1] + 5
    
        elif key == curses.KEY_DOWN:
            #screen.addstr(0, 0, "Down")
            if speed[0] > 35:
                speed[0] = speed[0] - 5
            if speed[1] > 162:
                speed[1] = speed[1] - 5
    
        elif key == curses.KEY_LEFT:
            #screen.addstr(0, 0, "Left")
            speed[0] = 64
            if speed[1] < 212:
                speed[1] = speed[1] + 5
 
        elif key == curses.KEY_RIGHT:
            #screen.addstr(0, 0, "Right")
            if speed[0] < 94:
                speed[0] = speed[0] + 5
            speed[1] = 192

    #serialWrite(serialport, [64, 192])
    screen.addstr(0, 0, '{} {}'.format(speed[0], speed[1]))
    if not pressed:
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

    sleep(0.1)

serialport.close()
curses.endwin()

