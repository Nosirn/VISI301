import pygame
import math
from bullet import Bullet

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('images/spritejoueur.png')
        self.image = self.get_image(56, 0)
        self.image_rotated = self.image
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        #self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.images = {'hand' : self.get_image(0,0),
                       'pistol' : self.get_image(56,0),
                       'smg' : self.get_image(112,0)}
        self.weapon = self.pistol()
        self.munition = 50
        self.cool_down_count = 0
        self.player_kill = False
        self.coin = 0
        self.health = 5

    def get_position(self):
        '''récupère la position du joueur'''
        return [self.position[0], self.position[1]]

    def save_location(self): self.old_position = self.position.copy()

    def move_right(self): self.position[0] += 3

    def move_left(self): self.position[0] -= 3

    def move_up(self): self.position[1] -= 3

    def move_down(self): self.position[1] += 3

    def update(self):
        '''met à jour le sprite'''
        posMouseX = pygame.mouse.get_pos()[0]
        posMouseY = pygame.mouse.get_pos()[1]
        deltaY = posMouseY - self.position[1]
        deltaX = posMouseX - self.position[0]
        angleInDegrees = math.atan2(deltaY , deltaX) * 180 / math.pi
        angleInDegrees = angleInDegrees + 90

        self.rect.topleft = self.position
        self.image = pygame.transform.rotozoom(self.image_rotated, -angleInDegrees, 1)
        self.rect = self.image.get_rect(center = (self.position[0],self.position[1]))
        self.image.set_colorkey([0, 0, 0])

    def move_back(self):
        '''Replace le joueur à son ancienne position si il atteint une zone de collision'''
        self.position = self.old_position
        self.rect.center = self.position
        #self.feet.midbottom = self.rect.midbottom

    def get_image(self, x, y):
        '''dessine le srite'''
        image = pygame.Surface([55, 95])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 55, 95))

        return image

    def cooldown(self):
        if self.cool_down_count >= 10:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def can_shoot(self):
        self.cooldown()
        return self.magazine > 0 and self.cool_down_count == 0

    def create_bullet(self):
        '''apelle une bullet'''
        self.magazine -= 1
        print(self.magazine)
        self.cool_down_count = 1
        return Bullet(self.position[0], self.position[1])

    def change_weapon(self, skin):
        '''change le skin selon l'arme'''
        self.image = self.images[skin]
        self.image.set_colorkey([0, 0, 0])
        self.image_rotated = self.image

    def pistol(self):
        '''capacité du chargeur'''
        self.capacity_max = 7
        self.magazine = 0

    def smg(self):
        '''capacité du chargeur'''
        self.capacity_max = 20
        self.magazine = 0

    def hand(self):
        '''capacité du chargeur'''
        self.capacity_max = 0
        self.magazine = 0

    def reload(self):
        while self.magazine < self.capacity_max and self.munition > 0:
            self.magazine += 1
            self.munition -= 1
        print("chargeur", self.magazine)
        print("mun restantes", self.munition)

    def get_coin(self):
        self.coin += 1
        print("coin : ", self.coin)

    #def degat(self):
