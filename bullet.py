import pygame
from PIL import Image
import math


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.position = [x, y]
        self.sprite_sheet = pygame.image.load('images/round_bullet.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.bullet_state = "ready"

    def get_position(self):
        return [self.position[0], self.position[1]]

    def save_location(self): self.old_position = self.position.copy()

    def move(self, cibleX, cibleY):
        x, y = self.position
        # caclul l'angle en radian
        angle = math.atan2(cibleY - y, cibleX - x)
        print("Angle en degrées :", int(angle * 180 / math.pi))
        newX = math.cos(angle)
        newY = math.sin(angle)

        self.position[0] = self.position[0] + int(newX)
        self.position[1] = self.position[1] + int(newY)
        print(self.position)

    def update(self):
        self.rect.topleft = self.position

    # Replace le joueur à son ancienne position si il atteint une zone de collision
    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def get_image(self, x, y):
        image = pygame.Surface([16, 16])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 16, 16))
        return image

    def rotate(self, img, rect, angle):
        self.rot_image = pygame.transform.rotate(img, angle)
        return self.rot_image
