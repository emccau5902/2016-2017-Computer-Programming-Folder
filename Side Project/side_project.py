# Computer Programming 1
# Unit 11 - Graphics
#
# Side Project


# Imports
import pygame
import intersects1
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Side Project"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (240, 0, 0)
GREEN = (0, 100, 0)
GRAY = (110, 110, 110)
BLUE = (75, 200, 255)
YELLOW = (240, 240, 140)

circle = [625, 125, 50]

case = 1

# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     
                
    # Game logic
    mouse_pos = pygame.mouse.get_pos()
    circle2 = [mouse_pos[0], mouse_pos[1], 50]
    
    if case == 1:
        if intersects1.point_circle(mouse_pos, circle):
            color = RED
        else:
            color = YELLOW

       
    # Drawing code
    ''' sky '''
    screen.fill(BLACK)

    if case == 1:
        pygame.draw.circle(screen, color, [circle[0], circle[1]], circle[2])

    ''' grass '''
    
    pygame.draw.rect(screen, GREEN, [0, 405, 800, 200])
    
    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, GRAY, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
        
    pygame.draw.line(screen, GRAY, [0, y+10], [800, y+10], 5)
    pygame.draw.line(screen, GRAY, [0, y+30], [800, y+30], 5)

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
