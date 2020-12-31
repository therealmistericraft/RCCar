import pygame
import RPi.GPIO as GPIO
from time import sleep as sleep


# Start Pygame in window (to have a "GUI" for the keyboard input)
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("RCCar control-interface")

"""
Forwards: GPIO 7
Backwards: GPIO 11
Right: GPIO 9
Left: GPIO 10
"""


# We are using GPIO numbering in this program
GPIO.setmode(GPIO.BCM)


# Setup necessary GPIOs as outputs (only needed after restart)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)


# define "shortcuts" for powering / unpowering GPIOs
def power(pin):
    GPIO.output(pin, GPIO.HIGH)

def unpower(pin):
    GPIO.output(pin, GPIO.LOW)

def steer(gpio):
    on(gpio)
    sleep(1)
    unpower(gpio)

carryOn = True


# This clock will be used to control how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while carryOn:

    # --- Main event loop
    for event in pygame.event.get(): # event-listener; detects interaction with controls
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False # Flag that we are done so we exit this loop

        # Start event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                power(7)

            if event.key == pygame.K_DOWN:
                power(11)

            # Steering: on keydown, full impact, hold position
            if event.key == pygame.K_RIGHT:
                t = threading.Thread(target=steer(9))
                t.start()

            # Steering: on keydown, full impact, hold position
            if event.key == pygame.K_LEFT:
                t = threading.Thread(target=steer(10))
                t.start()

        # Stop event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                unpower(7)

            if event.key == pygame.K_DOWN:
                unpower(11)

            # Steering: on keyup, impact to standby (0 degrees)
            if event.key == pygame.K_RIGHT:
                t = threading.Thread(target=steer(10))
                t.start()

            # Steering: on keyup, impact to standby (0 degrees)
            if event.key == pygame.K_LEFT:
                t = threading.Thread(target=steer(9))
                t.start()

     # --- Limit window-update-rate to 60 frames per second
        clock.tick(60)


#Once we have exited the main program loop we can stop the engine (pygame):
pygame.quit()
