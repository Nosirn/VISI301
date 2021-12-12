import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('images/spritejoueur.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.images = {'hand' : self.get_image(0,0),
                    'pistol' : self.get_image(56,0),
                    'smg' : self.get_image(112,0)}
        self.munition = 50
        self.capacity = 10
        self.weapon = "pistol"
        self.listweapon = ["hand", "pistol", "smg"]


    def get_position(self):
        return [self.position[0], self.position[1]]

    def save_location(self): self.old_position = self.position.copy()

    def move_right(self): self.position[0] += 3

    def move_left(self): self.position[0] -= 3

    def move_up(self): self.position[1] -= 3

    def move_down(self): self.position[1] += 3

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    # Replace le joueur à son ancienne position si il atteint une zone de collision
    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def get_image(self, x, y):
        image = pygame.Surface([55, 95])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 55, 95))
        return image
    
    def create_bullet(self):
        return Bullet(self.position[0], self.position[1])
    
    def change_weapon(self, skin):
        self.image = self.images[skin]
        self.image.set_colorkey([0, 0, 0])
    
    def rotate(self):
        