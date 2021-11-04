import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('images/player.png')
        self.image = self.get_image(46, 25)
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()
        self.position = [x, y]

    def move_right(self): self.position[0] += 3

    def move_left(self): self.position[0] -= 3

    def move_up(self): self.position[1] -= 3

    def move_down(self): self.position[1] += 3

    def update(self):
        self.rect.topleft = self.position

    def get_image(self, x, y):
        image = pygame.Surface([45, 70])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 45, 70))
        return image
