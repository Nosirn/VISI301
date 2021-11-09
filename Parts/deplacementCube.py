import pygame

def deplacerCube(LARGEUR, HAUTEUR, LARGEUR_CUBE, HAUTEUR_CUBE, VELOCITE):
    '''Déplace un cube dans une zone donnée
    Entrées :
    LARGEUR, HAUTEUR : Largeur et Hauteur de l'écran (en pixel) : Entier
    LARGEUR_CUBE, HAUTEUR_CUBE : Largeur et hauteur du cube (en pixel) : Entier
    VELOCITE : Distance de déplacement du cube (en pixel) : Entier
    Sortie : Rien
    '''
    ecran = pygame.display.set_mode((LARGEUR,HAUTEUR))
    
    x = LARGEUR//2
    y = HAUTEUR//2
    
    widthCube = LARGEUR_CUBE
    heightCube = HAUTEUR_CUBE
      
    vel = VELOCITE
      
    run = True
      
    while run:

        #Délai
        pygame.time.delay(20)
        keys = pygame.key.get_pressed()
        
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
        
        ecran.fill((0, 12, 0))
        pygame.draw.rect(ecran, (255, 0, 0), (x, y, widthCube, heightCube)) 
        pygame.display.update()  
      
    return

if __name__ == '__main__':

    Lar = 1280 #Largeur écran
    Hau = 720 #Hauteur écran
    
    ecran = pygame.display.set_mode((Lar, Hau)) 
    pygame.display.set_caption("Moving rectangle")
    
    deplacerCube(Lar,Hau,20,20,10)
    pygame.quit()

