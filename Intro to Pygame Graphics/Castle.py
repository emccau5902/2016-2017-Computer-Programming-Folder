# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
''' add colors you use as RGB values here '''
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
DARK_GREEN = (0, 150, 0)
GRAY = (70, 70, 70)
DARK_GRAY = (45, 45, 45)
LIGHT_GRAY = (81, 81, 81)

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 


    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)
    pygame.draw.rect(screen, DARK_GREEN, [0, 460, 800, 600])

    pygame.draw.rect(screen, GRAY, [150, 280, 450, 220])

    pygame.draw.rect(screen, GRAY, [140, 270, 470, 70])

    pygame.draw.rect(screen, DARK_GRAY, [280, 190, 190, 80])
    pygame.draw.rect(screen, DARK_GRAY, [270, 160, 30, 70])
    pygame.draw.rect(screen, DARK_GRAY, [320, 163, 40, 70])
    pygame.draw.rect(screen, DARK_GRAY, [390, 163, 40, 70])
    pygame.draw.rect(screen, DARK_GRAY, [450, 160, 30, 70])
    
    pygame.draw.rect(screen, GRAY, [140, 240, 30, 100])
    pygame.draw.rect(screen, GRAY, [190, 243, 30, 100])
    pygame.draw.rect(screen, GRAY, [240, 243, 30, 100])
    pygame.draw.rect(screen, GRAY, [280, 243, 30, 100])
    pygame.draw.rect(screen, GRAY, [330, 243, 30, 100])
    pygame.draw.rect(screen, GRAY, [390, 243, 30, 100])
    pygame.draw.rect(screen, GRAY, [440, 243, 30, 100])
    pygame.draw.rect(screen, GRAY, [480, 243, 30, 100])
    pygame.draw.rect(screen, GRAY, [530, 243, 30, 100])
    pygame.draw.rect(screen, GRAY, [580, 240, 30, 100])


    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
