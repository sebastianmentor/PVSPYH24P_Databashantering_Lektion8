import pygame     #import the module
from led import mlcdinit,mlcddraw

mlcdinit(16,3,3) # initialize a 16x3 display scaled 3x  

#draw the three lines passed as a list
mlcddraw(["Hello",         
               "     world",
               "What"])

while True:
    for event in pygame.event.get():
        pass