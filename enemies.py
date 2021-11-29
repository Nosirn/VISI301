import pygame
from player import Player

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, cible):
        super().__init__()
        self.sprite_sheet = pygame.image.load('images/soldier.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.change_position = [0, 0]
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.speed = 1


    def get_position(self):
        return [self.position[0], self.position[1]]

    def save_location(self): self.old_position = self.position.copy()

    def move_right(self): self.change_position[0] += self.speed

    def move_left(self): self.change_position[0] -= self.speed

    def move_up(self): self.change_position[1] -= self.speed

    def move_down(self): self.change_position[1] += self.speed

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    # Replace le sprite à son ancienne position si il atteind une zone de collision
    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def get_image(self, x, y):
        image = pygame.Surface([64, 64])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 64, 64))
        return image

    def follow_player(self, cible):

        if self.get_position()[0] > cible[0]:
            self.move_left()
        elif self.get_position()[0] < cible[0]:
            self.move_right()
        if self.get_position()[1] > cible[1]:
            self.move_up()
        elif self.get_position()[1] < cible[1]:
            self.move_down()

        self.position[0] += self.change_position[0]
        self.position[1] += self.change_position[1]
        self.change_position = [0, 0]




