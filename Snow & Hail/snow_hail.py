# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make snow and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Snow and Hail"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (0, 100, 0)
WHITE = (255, 255, 255)
GRAY = (110, 110, 110)
BLUE = (75, 200, 255)
BLACK = (0, 0, 0)
YELLOW = (240, 240, 140)


def draw_snow(x, y):
    pygame.draw.ellipse(screen, WHITE, s)
def hail(x, y):
    pygame.draw.ellipse(screen, WHITE, h)


''' make snow '''

snow = []
for i in range(450):
    x = random.randrange(0, 800)
    y = random.randrange(0, 400)
    r = random.randrange(1,5)
    snow.append([x, y, r, r])

hail = []
for i in range(20):
    x = random.randrange(0, 800)
    y = random.randrange(0, 400)
    r = random.randrange(8,12)
    hail.append([x, y, r, r])




# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     
                
    # Game logic
    
    ''' move snow '''
    for s in snow:
        s[1] += 1
        s[0] += 1
        

        if s[1] > 400:
            s[1] = random.randrange(-10, 0)
            s[0] = random.randrange(0, 800)
        if s[0] > 800:
            s[0] = random.randrange(-10, 0)
            s[1] = random.randrange(0, 600)

            
    for h in hail:
        h[1] += 4
        h[0] += 2
        
        
        if h[1] > 400:
            h[1] = random.randrange(-10, 0)
            h[0] = random.randrange(0, 800)
            
        if h[0] > 800:
            h[0] = random.randrange(-10, 0)
            h[1] = random.randrange(0, 600)
        

            
    # Drawing code
    ''' sky '''
    screen.fill(BLACK)

    ''' moon '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])
    
    ''' snow '''
    for s in snow:
        pygame.draw.ellipse(screen, WHITE, s)
    for h in hail:
        pygame.draw.ellipse(screen, WHITE, h)

    ''' grass '''
    
    pygame.draw.rect(screen, GREEN, [0, 405, 800, 200])
    pygame.draw.rect(screen, WHITE, [0, 403, 800, 23])
    
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
