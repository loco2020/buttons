# -- import (pygame) models
import pygame

 # initialization pygame to start  ---->
pygame.init()

clock = pygame.time.Clock() # Fps -->

Fps = 30
screen_w = 680 # screen highet
screen_h = 680 # screen width

# set window ---->
win = pygame.display.set_mode((screen_w,screen_h)) 
pygame.display.set_caption("Button") # Title -->
font = pygame.font.SysFont('Arial',38,True)

rect = pygame.Rect(0,0,200,60)
rect.midtop = win.get_rect().center
text = "Click me"
conter = 0
run = True
# Main Loop --->
while run:
    clock.tick(Fps)
    
    # Chack The Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if quit then close the game
            run = False

        px,py = pygame.mouse.get_pos()
        if rect.collidepoint(px,py):
            if event.type == pygame.MOUSEBUTTONDOWN:
                text = "You Clicked"
                conter += 1
                print(text+" "+str(conter))

    pygame.draw.rect(win,(230,230,230),rect)
    click = font.render(text,1,(30,30,30))
    pos = click.get_rect(center=rect.center)
    win.blit(click,pos)
    pygame.display.update()
    win.fill((100,200,200))
pygame.quit()