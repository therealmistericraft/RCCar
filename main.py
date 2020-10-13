import pygame
import RPi.GPIO as GPIO
import time



events = pygame.event.get()
for event in events:
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
                        
