import pygame
import random

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 800))

# Title and icon
pygame.display.set_caption("CMI-zombie")
icon = pygame.image.load('images/zombie.png')
pygame.display.set_icon(icon)


# player
playerIMG = pygame.image.load('images/soldier.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy

enemyIMG = pygame.image.load('images/zombie.png')
enemyX = random.randint(0,736)
enemyY = random.randint(0,736)
enemyX_change = 0
enemyY_change = 0


def player(x, y):
    screen.blit(playerIMG, (x, y))


def enemy(x, y):
    screen.blit(enemyIMG, (x, y))



# Game loop
running = True
while running:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.8
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.8
            if event.key == pygame.K_UP:
                playerY_change = -0.8
            if event.key == pygame.K_DOWN:
                playerY_change = 0.8

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if playerY <= 0:
        playerY = 0
    elif playerY >= 736:
        playerY = 736

    #deplacement enemie

    if enemyX > playerX:
        enemyX_change = -0.3
    elif enemyX < playerX:
        enemyX_change = 0.3

    if enemyY > playerY:
        enemyY_change = -0.3
    elif enemyY < playerY:
        enemyY_change = 0.3

    enemyX += enemyX_change
    enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX,enemyY)

    pygame.display.update()
