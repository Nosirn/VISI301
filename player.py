import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('images/spritejoueur.png')
        self.image = self.get_image(56, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.images = {'hand' : self.get_image(0,0),
                       'pistol' : self.get_image(56,0),
                       'smg' : self.get_image(112,0)}
        self.weapon = self.pistol()
        self.munition = 50


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
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        '''Replace le joueur à son ancienne position si il atteint une zone de collision'''
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def get_image(self, x, y):
        '''dessine le srite'''
        image = pygame.Surface([55, 95])
        posMouseX = pygame.mouse.get_pos()[0]
        posMouseY = pygame.mouse.get_pos()[1]
        angle = 45

        image.blit(self.sprite_sheet, (0, 0), (x, y, 55, 95))

        return image

    def can_shoot(self):
        if self.magazine > 0:
            res = True
        else:
            res = False
        return res

    def create_bullet(self):
        '''apelle une bullet'''
        self.magazine -= 1
        print(self.magazine)
        return Bullet(self.position[0], self.position[1])


    def change_weapon(self, skin):
        '''change le skin selon l'arme'''
        self.image = self.images[skin]
        self.image.set_colorkey([0, 0, 0])

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