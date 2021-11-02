import pygame

pygame.init()

class player():
    playerIMG = pygame.image.load('images/soldier.png')
    playerX = 370
    playerY = 480
    playerX_change = 0
    playerY_change = 0