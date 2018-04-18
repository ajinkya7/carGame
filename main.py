import pygame

pygame.init()

#Window Dimensions
display_width = 800
display_height = 600

#Colours
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
block_color = (53,115,255)

#Window 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Car Fury')

#Clock
clock = pygame.time.Clock()

#Loading Pictures
carImg = pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    car(20,100)

        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
