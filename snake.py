import pygame
import sys
import time
import random
import pyttsx3

# pyttsx3 config
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

try:
    print()
    speak('Welcome to The Snake.')
    speak('Connection successfully established. Now you may play.')

    # Pygame Init
    init_status = pygame.init()
    if init_status[1] > 0:
        print("(!) Had {0} initialising errors, exiting... ".format(init_status[1]))
        sys.exit()
    else:
        print("Pygame initialised successfully ")

    # Play Surface
    size = width, height = 640, 400
    playSurface = pygame.display.set_mode(size)
    pygame.display.set_caption("Snake Game")
    pygame.display.set_icon(pygame.image.load('snake.png'))


    # Colors
    red = pygame.Color('red')
    green = pygame.Color('green')
    black = pygame.Color('black')
    white = pygame.Color('white')
    brown = pygame.Color('brown')

    # FPS controller
    fpsController = pygame.time.Clock()

    # Game settings
    delta = 10
    snakePos = [100, 50]
    snakeBody = [[100, 50], [90, 50], [80, 50]]
    foodPos = [400, 50]
    foodSpawn = True
    direction = 'RIGHT'
    change_to = ''
    score = 0


    # Game Over
    def game_over():
        myFont = pygame.font.SysFont('monaco', 72)
        GOsurf = myFont.render("Game Over", True, red)
        GOrect = GOsurf.get_rect()
        GOrect.midtop = (320, 25)
        playSurface.blit(GOsurf, GOrect)
        show_score(0)
        pygame.display.flip()
        time.sleep(4)
        pygame.quit()


    # Show Score
    def show_score(choice=1):
        SFont = pygame.font.SysFont('monaco', 32)
        Ssurf = SFont.render("Score  :  {0}".format(score), True, white)
        Srect = Ssurf.get_rect()
        if choice == 1:
            Srect.midtop = (80, 10)
        else:
            Srect.midtop = (320, 100)
        playSurface.blit(Ssurf, Srect)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    change_to = 'RIGHT'
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    change_to = 'LEFT'
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    change_to = 'DOWN'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        # Validate direction
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = change_to
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = change_to
        if change_to == 'UP' and direction != 'DOWN':
            direction = change_to
        if change_to == 'DOWN' and direction != 'UP':
            direction = change_to

        # Update snake position
        if direction == 'RIGHT':
            snakePos[0] += delta
        if direction == 'LEFT':
            snakePos[0] -= delta
        if direction == 'DOWN':
            snakePos[1] += delta
        if direction == 'UP':
            snakePos[1] -= delta

        # Snake body mechanism
        snakeBody.insert(0, list(snakePos))
        if snakePos == foodPos:
            foodSpawn = False
            score += 1
        else:
            snakeBody.pop()
        if foodSpawn == False:
            foodPos = [random.randrange(1, width // 10) * delta, random.randrange(1, height // 10) * delta]
            foodSpawn = True

        playSurface.fill(black)
        for pos in snakeBody:
            pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], delta, delta))
        pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], delta, delta))

        # Bounds
        if snakePos[0] >= width or snakePos[0] < 0:
            game_over()
        if snakePos[1] >= height or snakePos[1] < 0:
            game_over()

        # Self hit
        for block in snakeBody[1:]:
            if snakePos == block:
                game_over()

        pygame.display.flip()
        fpsController.tick(20)

except Exception as e:
    import handler
print()
