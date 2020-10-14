import pygame
import RPi.GPIO as GPIO
from time import sleep as sleep

# Start Pygame in window
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("RCCar control-interface")

# Forewards: GPIO 7
# Backwards: GPIO 11
# Right: GPIO 9
# Left: GPIO 10

# Setup GPIO
GPIO.setmode(GPIO.BCM)
# Setup GPIOs as outputs (only needed after restart)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

# Shorten GPIO activator/deactivator
def on(pin):
    GPIO.output(pin, GPIO.HIGH)
def off(pin):
    GPIO.output(pin, GPIO.LOW)

carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False # Flag that we are done so we exit this loop
        # Start event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                on(7)
            if event.key == pygame.K_DOWN:
                on(11)
            # Steering: on keydown, full impact, hold position
            if event.key == pygame.K_RIGHT:
                on(9)
                sleep(1)
                off(9)
        # Stop event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                off(7)
            if event.key == pygame.K_DOWN:
                off(11)
            # Steering: on keyup, impact to standby (0 degrees)
            if event.key == pygame.K_RIGHT:
                on(10)
                sleep(1)
                off(10)
     
     # --- Limit to 60 frames per second
        clock.tick(1)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
