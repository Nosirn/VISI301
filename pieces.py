import pygame
from random import *

res = (1280, 720)

#implémentation du fichier piece

class Piece(pygame.sprite.Sprite):
    '''Crée une pièce
       x,y : Position initiale de la pièce (Défaut : x=0;y=0)
       radius : Taille de la pièce (Défaut : 1)
    '''

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([x, y])
        self.rect = self.image.get_rect()

    def modifierPosition(self):
        '''Modifie la position de la pièce aléatoirement'''
        self.position[0] = randrange(0 + self.radius, res[0] + 1 - self.radius, 2)
        self.position[1] = randrange(0 + self.radius, res[1] + 1 - self.radius, 2)

    def Touche(self, player):
        '''Vérifie si un joueur touche la pièce
           player : Joueur
        '''
        if (player.position[0] >= self.position[0] - self.radius and player.position[0] <= self.position[
            0] + self.radius and player.position[1] >= self.position[1] - self.radius and player.position[1] <=
                self.position[1] + self.radius):
            STATUS = True
        else:
            STATUS = False
        return STATUS

    def Draw(self, screen):
        '''Dessine la pièce'''
        pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), self.radius)

