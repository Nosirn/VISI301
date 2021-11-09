import pygame
from random import *

def AfficherPiece(LARGEUR, HAUTEUR, LARGEUR_CUBE, HAUTEUR_CUBE, VELOCITE, RAYON_PIECE):

    #Taille de l'écran
    ecran = pygame.display.set_mode((LARGEUR,HAUTEUR))

    #Position du cube
    x = LARGEUR//2
    y = HAUTEUR//2

    #Taille et vitesse du cube
    widthCube = LARGEUR_CUBE
    heightCube = HAUTEUR_CUBE
    vel = VELOCITE

    #Taille de la pièce
    radiusCoin = RAYON_PIECE
    
    posCoinX = randrange(0+radiusCoin, LARGEUR+1-radiusCoin, 2)
    posCoinY = randrange(0+radiusCoin, HAUTEUR+1-radiusCoin, 2)
    
    Touche = False

    #Affichage
    ecran.fill((0, 12, 0))
    pygame.draw.rect(ecran, (255, 0, 0), (x, y, widthCube, heightCube))
    pygame.draw.circle(ecran, (255, 255, 0), (posCoinX, posCoinY), radiusCoin)
    pygame.display.update() 
                        
    run = True
      
    while run:

        #Délai
        pygame.time.delay(2)
        keys = pygame.key.get_pressed()

        #Quitter
        for event in pygame.event.get(): 
            if keys[pygame.K_q]:
                run = False
          
        #Déplacement Gauche
        if keys[pygame.K_LEFT] and x>0:
            x -= vel 

        #Déplacement Droite
        if keys[pygame.K_RIGHT] and x<LARGEUR-widthCube: 
            x += vel 
             
        #Déplacement Haut
        if keys[pygame.K_UP] and y>0: 
            y -= vel 
              
        #Déplacement Bas
        if keys[pygame.K_DOWN] and y<HAUTEUR-heightCube:
            y += vel 

        #Pièce
        if(x >= posCoinX-radiusCoin-(widthCube/2) and x <= posCoinX+radiusCoin+(widthCube/2) and
           y >= posCoinY-radiusCoin-(heightCube/2) and y <= posCoinY+radiusCoin+(heightCube/2)):

            print("  ")
            print("x",x,"y",y)
            print("posCoinX",posCoinX,"posCoinY",posCoinY)
            print("x >= ", posCoinX-radiusCoin-(widthCube/2))
            print("x <= ", posCoinX+radiusCoin+(widthCube/2))
            print("y >= ", posCoinY-radiusCoin-(heightCube/2))
            print("y <= ", posCoinY+radiusCoin+(heightCube/2))

            posCoinX = randrange(0+radiusCoin, LARGEUR+1-radiusCoin, 2)
            posCoinY = randrange(0+radiusCoin, HAUTEUR+1-radiusCoin, 2)

                
        
        #Affichage
        ecran.fill((0, 12, 0))
        pygame.draw.rect(ecran, (255, 0, 0), (x, y, widthCube, heightCube))
        pygame.draw.circle(ecran, (255, 255, 0), (posCoinX, posCoinY), radiusCoin)
        pygame.display.update() 
    
    return


if __name__ == '__main__':

    Lar = 1280 #Largeur écran
    Hau = 720 #Hauteur écran
    
    ecran = pygame.display.set_mode((Lar, Hau)) 
    pygame.display.set_caption("Moving rectangle")
    
    AfficherPiece(Lar,Hau,15,15,1,5)
    pygame.quit()

