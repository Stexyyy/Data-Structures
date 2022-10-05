import pygame
import time
pygame.init()
pygame.display.set_caption("data structures (lists)")
screenSize = (800, 800)
screen = pygame.display.set_mode(screenSize) #creates the obvious game screen

Purple = (255, 0, 255) #prime example of a tuple

#lists can contain tuples!
#you can also change lists unlike tuples!

daCircle = [(100, 200), (300, 400), (100, 400), (500, 600), (500, 300)] #a list with tuples in it

for i in range (len(daCircle)): #looks at the length of my list
    pygame.draw.circle(screen, Purple, (daCircle[i]), 50)



pygame.display.flip()
time.sleep(100)
