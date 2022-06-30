from turtle import width
import pygame

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0 

def redrawWindow():
    win.fill(255, 255, 255)
    pygame.display.update()