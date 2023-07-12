import pygame, sys, random
from testing1 import *
from pygame.locals import *
pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 850
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')
 
# The main function that controls the game
def main () :
  looping = True
  
  # The main game loop
  while looping :
    # Get inputs
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
    
    # Processing
    # This section will be built out later
    RED = (255, 0, 0)
    BLACK = (0,0,0)
    GREEN = (0, 255, 0)
    WHITE = (255,255,255)
    BLUE = (0, 0, 255)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)	

    rectangle1 = pygame.Rect(50, 90, 400, 400)

    #RED Face
    Rrectangle1 = pygame.Rect(150, 100, 30, 30)
    Rrectangle2 = pygame.Rect(180, 100, 30, 30)
    Rrectangle3 = pygame.Rect(210, 100, 30, 30)
    Rrectangle4 = pygame.Rect(150, 130, 30, 30)
    Rrectangle5 = pygame.Rect(180, 130, 30, 30)
    Rrectangle6 = pygame.Rect(210, 130, 30, 30)
    Rrectangle7 = pygame.Rect(150, 160, 30, 30)
    Rrectangle8 = pygame.Rect(180, 160, 30, 30)
    Rrectangle9 = pygame.Rect(210, 160, 30, 30)
   
    #White Face
    Wrectangle1 = pygame.Rect(150, 190, 30, 30)
    Wrectangle2= pygame.Rect(180, 190, 30, 30)
    Wrectangle3= pygame.Rect(210, 190, 30, 30)
    Wrectangle4= pygame.Rect(150, 220, 30, 30)
    Wrectangle5= pygame.Rect(180, 220, 30, 30)
    Wrectangle6= pygame.Rect(210, 220, 30, 30)
    Wrectangle7= pygame.Rect(150, 250, 30, 30)
    Wrectangle8= pygame.Rect(180, 250, 30, 30)
    Wrectangle9= pygame.Rect(210, 250, 30, 30)

    #Green Face
    Grectangle1 = pygame.Rect(60, 190, 30, 30)
    Grectangle2= pygame.Rect(90, 190, 30, 30)
    Grectangle3= pygame.Rect(120, 190, 30, 30)
    Grectangle4 = pygame.Rect(60, 220, 30, 30)
    Grectangle5= pygame.Rect(90, 220, 30, 30)
    Grectangle6= pygame.Rect(120, 220, 30, 30)
    Grectangle7 = pygame.Rect(60, 250, 30, 30)
    Grectangle8= pygame.Rect(90, 250, 30, 30)
    Grectangle9= pygame.Rect(120, 250, 30, 30)
    
    #Orange Face
    Orectangle1 = pygame.Rect(150, 280, 30, 30)
    Orectangle2= pygame.Rect(180, 280, 30, 30)
    Orectangle3= pygame.Rect(210, 280, 30, 30)
    Orectangle4= pygame.Rect(150, 310, 30, 30)
    Orectangle5= pygame.Rect(180, 310, 30, 30)
    Orectangle6= pygame.Rect(210, 310, 30, 30)
    Orectangle7= pygame.Rect(150, 340, 30, 30)
    Orectangle8= pygame.Rect(180, 340, 30, 30)
    Orectangle9= pygame.Rect(210, 340, 30, 30)

    #Blue Face
    Brectangle1 = pygame.Rect(240, 190, 30, 30)
    Brectangle2= pygame.Rect(270, 190, 30, 30)
    Brectangle3= pygame.Rect(300, 190, 30, 30)
    Brectangle4= pygame.Rect(240, 220, 30, 30)
    Brectangle5= pygame.Rect(270, 220, 30, 30)
    Brectangle6= pygame.Rect(300, 220, 30, 30)
    Brectangle7= pygame.Rect(240, 250, 30, 30)
    Brectangle8= pygame.Rect(270, 250, 30, 30)
    Brectangle9= pygame.Rect(300, 250, 30, 30)

    #Yellow Face
    Yrectangle1 = pygame.Rect(330, 190, 30, 30)
    Yrectangle2= pygame.Rect(360, 190, 30, 30)
    Yrectangle3= pygame.Rect(390, 190, 30, 30)
    Yrectangle4= pygame.Rect(330, 220, 30, 30)
    Yrectangle5= pygame.Rect(360, 220, 30, 30)
    Yrectangle6= pygame.Rect(390, 220, 30, 30)
    Yrectangle7= pygame.Rect(330, 250, 30, 30)
    Yrectangle8= pygame.Rect(360, 250, 30, 30)
    Yrectangle9= pygame.Rect(390, 250, 30, 30)


    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    pygame.draw.rect(WINDOW, BLACK, rectangle1, 2)

    
    #Red Face
    pygame.draw.rect(WINDOW, RED, Rrectangle1, 2)
    pygame.draw.rect(WINDOW, RED, Rrectangle2, 2)
    pygame.draw.rect(WINDOW, RED, Rrectangle3, 2)
    pygame.draw.rect(WINDOW, RED, Rrectangle4, 2)
    pygame.draw.rect(WINDOW, RED, Rrectangle5, 2)
    pygame.draw.rect(WINDOW, RED, Rrectangle6, 2)
    pygame.draw.rect(WINDOW, RED, Rrectangle7, 2)
    pygame.draw.rect(WINDOW, RED, Rrectangle8, 2)
    pygame.draw.rect(WINDOW, RED, Rrectangle9, 2)
    
    #WhiteFace
    pygame.draw.rect(WINDOW, BLACK, Wrectangle1, 2)
    pygame.draw.rect(WINDOW, BLACK, Wrectangle2, 2)
    pygame.draw.rect(WINDOW, BLACK, Wrectangle3, 2)
    pygame.draw.rect(WINDOW, BLACK, Wrectangle4, 2)
    pygame.draw.rect(WINDOW, BLACK, Wrectangle5, 2)
    pygame.draw.rect(WINDOW, BLACK, Wrectangle6, 2)
    pygame.draw.rect(WINDOW, BLACK, Wrectangle7, 2)
    pygame.draw.rect(WINDOW, BLACK, Wrectangle8, 2)
    pygame.draw.rect(WINDOW, BLACK, Wrectangle9, 2)
    
    #Green Face
    pygame.draw.rect(WINDOW, GREEN, Grectangle1, 2)
    pygame.draw.rect(WINDOW, GREEN, Grectangle2, 2)
    pygame.draw.rect(WINDOW, GREEN, Grectangle3, 2)
    pygame.draw.rect(WINDOW, GREEN, Grectangle4, 2)
    pygame.draw.rect(WINDOW, GREEN, Grectangle5, 2)
    pygame.draw.rect(WINDOW, GREEN, Grectangle6, 2)
    pygame.draw.rect(WINDOW, GREEN, Grectangle7, 2)
    pygame.draw.rect(WINDOW, GREEN, Grectangle8, 2)
    pygame.draw.rect(WINDOW, GREEN, Grectangle9, 2)
    
    #Orange Face
    pygame.draw.rect(WINDOW, ORANGE, Orectangle1, 2)
    pygame.draw.rect(WINDOW, ORANGE, Orectangle2, 2)
    pygame.draw.rect(WINDOW, ORANGE, Orectangle3, 2)
    pygame.draw.rect(WINDOW, ORANGE, Orectangle4, 2)
    pygame.draw.rect(WINDOW, ORANGE, Orectangle5, 2)
    pygame.draw.rect(WINDOW, ORANGE, Orectangle6, 2)
    pygame.draw.rect(WINDOW, ORANGE, Orectangle7, 2)
    pygame.draw.rect(WINDOW, ORANGE, Orectangle8, 2)
    pygame.draw.rect(WINDOW, ORANGE, Orectangle9, 2)

    #Blue Face
    pygame.draw.rect(WINDOW, BLUE, Brectangle1, 2)
    pygame.draw.rect(WINDOW, BLUE, Brectangle2, 2)
    pygame.draw.rect(WINDOW, BLUE, Brectangle3, 2)
    pygame.draw.rect(WINDOW, BLUE, Brectangle4, 2)
    pygame.draw.rect(WINDOW, BLUE, Brectangle5, 2)
    pygame.draw.rect(WINDOW, BLUE, Brectangle6, 2)
    pygame.draw.rect(WINDOW, BLUE, Brectangle7, 2)
    pygame.draw.rect(WINDOW, BLUE, Brectangle8, 2)
    pygame.draw.rect(WINDOW, BLUE, Brectangle9, 2)
    
    #Yellow Face
    pygame.draw.rect(WINDOW, YELLOW, Yrectangle1, 2)
    pygame.draw.rect(WINDOW, YELLOW, Yrectangle2, 2)
    pygame.draw.rect(WINDOW, YELLOW, Yrectangle3, 2)
    pygame.draw.rect(WINDOW, YELLOW, Yrectangle4, 2)
    pygame.draw.rect(WINDOW, YELLOW, Yrectangle5, 2)
    pygame.draw.rect(WINDOW, YELLOW, Yrectangle6, 2)
    pygame.draw.rect(WINDOW, YELLOW, Yrectangle7, 2)
    pygame.draw.rect(WINDOW, YELLOW, Yrectangle8, 2)
    pygame.draw.rect(WINDOW, YELLOW, Yrectangle9, 2)
    
    
    
    
    
    
    pygame.display.update()
    fpsClock.tick(FPS)
    
   
   



main()