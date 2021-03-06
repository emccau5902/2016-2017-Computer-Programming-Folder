# Imports
import pygame


# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Game Stages Demo"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Fonts
MY_FONT = pygame.font.Font(None, 50)


# stages
START = 0
PLAYING = 1
END = 2


def setup():
    global block_pos, block_vel, size, stage
    
    block_pos = [375, 275]
    block_vel = [0, 0]
    size = 50

    stage = START


# Game loop
setup()
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                  
            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()


    if stage == PLAYING:
        pressed = pygame.key.get_pressed()

        up = pressed[pygame.K_UP]
        down = pressed[pygame.K_DOWN]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]
    
        if left:
            block_vel[0] = -4
        elif right:
            block_vel[0] = 4
        elif up:
            block_vel[1] = -4
        elif down:
            block_vel[1] = 4

    # Game logic
    if stage == PLAYING:
        ''' move block '''
        block_pos[0] += block_vel[0]
        block_pos[1] += block_vel[1]

        ''' end game on wall collision '''
        if block_pos[0] < 0 or block_pos[0] > 950 or \
           block_pos[1] < 0 or block_pos[1] > 650:
            stage = END
            
     
    # Drawing code
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [block_pos[0], block_pos[1], size, size]) 

    ''' begin/end game text '''
    if stage == START:
        text1 = MY_FONT.render("Block", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to play.)", True, WHITE)
        screen.blit(text1, [350, 150])
        screen.blit(text2, [225, 200])
    elif stage == END:
        text1 = MY_FONT.render("Game Over", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to restart.)", True, WHITE)
        screen.blit(text1, [310, 150])
        screen.blit(text2, [210, 200])


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)


# Close window on quit
pygame.quit()
