import time
import RPi.GPIO as GPIO
import curses

frequency = 100 # Hz
pin_m1 = 12
pin_m2 = 32

neutral = 13.9
first_gear = 13
second_gear = 12
reverse = 15

screen = curses.initscr()
curses.cbreak()
screen.keypad(1)

# set up RPi I/O
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_m1, GPIO.OUT)
GPIO.setup(pin_m2, GPIO.OUT)
p = GPIO.PWM(pin_m1, frequency)  
q = GPIO.PWM(pin_m2, frequency) 

p.start(neutral)
q.start(neutral)

dc = neutral
key = ''
while key != ord('q'):  # press <Q> to exit the program
    key = screen.getch()  # get the key
    screen.refresh()

    # the same, but for <Up> and <Down> keys:
    if key == curses.KEY_UP:
        dc = dc + 0.5
    elif key == curses.KEY_DOWN:
	dc = dc - 0.5

    screen.addstr(0, 0, str(dc))
    try:
	p.ChangeDutyCycle(dc)
        q.ChangeDutyCycle(dc)
    except KeyboardInterrupt:
        pass

curses.endwin()
p.stop()
q.stop()
GPIO.cleanup()
