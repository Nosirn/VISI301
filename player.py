import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('images/player.png')
        self.image = self.get_image(46, 25)
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()

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
        image = pygame.Surface([45, 65])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 45, 65))
        return image
