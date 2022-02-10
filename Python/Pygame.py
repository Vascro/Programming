import pygame, sys, random
from pygame.locals import *
pygame.init()
fps = 120
framepersec = pygame.time.Clock()
black = (0, 0, 0)
white = (255,255,255)
purple = (128,0,128)
playfield = pygame.display.set_mode((1280,720))
pygame.draw.circle(playfield, white, (500,200), 30)
pygame.draw.circle(playfield, white, (800,200), 30)
pygame.draw.circle(playfield, black, (500,200), 10)
pygame.draw.circle(playfield, black, (800,200), 10)
pygame.draw.line(playfield, purple, (500,400), (800,400))
#Game loop begins
while True:
    pygame.display.update()
    keypress = pygame.key.get_pressed()  
    for event in pygame.event.get():
        if event.type == keypress:
            pygame.quit()
            sys.exit()
    framepersec.tick(fps)