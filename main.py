import pygame
import RPi.GPIO as GPIO
from time import sleep as sleep

# Start Pygame in window
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("RCCar interface")

# Forewards: GPIO 7

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

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
        # Stop event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                off(7)
            if event.key == pygame.K_DOWN:
                off(11)
     
     # --- Limit to 60 frames per second
        clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
