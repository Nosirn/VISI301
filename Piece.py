import pygame
from random import *


class Piece(radius):
    def __init__(self):
        self.position = [x, y]
        self.radius = radius

    def Position(x,y):
        x,y = (randrange(0+radiusCoin, res[0]+1-radiusCoin, 2),randrange(0+radiusCoin, res[1]+1-radiusCoin, 2))
    
    def Touche(self, player, STATUS):
        if(player.position[0] >= self.position[0]-self.radius and player.position[0] <= self.position[0]+self.radius and
           player.position[1] >= self.position[1]-self.radius and player.position[1] <= self.position[1]+self.radius):
            STATUS = True
        else:
            STATUS = False
    
    

    #Pièce
    if(x >= posCoinX-radiusCoin-(widthCube/2) and x <= posCoinX+radiusCoin+(widthCube/2) and
    y >= posCoinY-radiusCoin-(heightCube/2) and y <= posCoinY+radiusCoin+(heightCube/2)):
                        
        score += 1
        print("  ")
        print("x",x,"y",y)
        print("posCoinX",posCoinX,"posCoinY",posCoinY)
        print("x >= ", posCoinX-radiusCoin-(widthCube/2))
        print("x <= ", posCoinX+radiusCoin+(widthCube/2))
        print("y >= ", posCoinY-radiusCoin-(heightCube/2))
        print("y <= ", posCoinY+radiusCoin+(heightCube/2))

    posCoinX = randrange(0+radiusCoin, screen_width-radiusCoin, 2)
    posCoinY = randrange(0+radiusCoin, screen_height-radiusCoin, 2)

    score_afficher = myfont.render(str(score), 1, (255,0,0))
    screen.blit(score_afficher, (100, 100))
    
    pygame.draw.circle(screen, (255, 255, 0), (posCoinX, posCoinY), radiusCoin)

    
