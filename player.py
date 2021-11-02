import pygame

class player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.sprite_sheet = pygame.image.load('images/soldier.png')



