import pygame
import RPi.GPIO as GPIO
import time

# Forewards: GPIO 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)

def on(pin):
    GPIO.output(pin, GPIO.HIGH)
def off(pin):
    GPIO.output(pin, GPIO.LOW)

events = pygame.event.get()
for event in events:
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            on(7)
