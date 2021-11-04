import pygame

#Initialisation pygame
pygame.init()

#Initialisation de la fenêtre
fenetre = pygame.display.set_mode((800,600))




class Projectile(pygame.sprite.Sprite):
    def init(self, posx_end, posy_end):
        pygame.sprite.Sprite.init(self) 
        self.image = pygame.image.load("sprite\feu.png")
        self.posx_end = posx_end
        self.posy_end = posy_end
        self.step = 5

        self.longx = self.posx_end - player.get_posx()
        self.longy = self.posy_end - player.get_posy()

    def maj_new_pos(self):
        """ Mets les positions du projectile à jours"""
        self.posx += self.stepmath.cos(math.atan2(self.longy, self.longx))
        self.posy += self.stepmath.sin(math.atan2(self.longy, self.longx))
        self.ttl += 1
        print("Compute position projectile")
        return self.posx, self.posy

    def draw(self, screen):
        """ Dessine le projectile sur la surface """
        print("Drawing new projectile")
        screen.blit(self.image, self.maj_new_pos())

while fin :

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = False
            pygame.quit()

    mouse_pos = pygame.mouse.get_pos()
    projectile_temp = Projectile(mouse_pos[0], mouse_pos[1])
