#Créé par : http://fr.wikibooks.org/w/index.php?title=Pygame/Concevoir_des_jeux_avec_Pygame&action=history
#Partie Thread : https://www.tutorialspoint.com/python/python_multithreading.htm#:~:text=Python%20-%20Multithreaded%20Programming.%20Multiple%20threads%20within%20a,more%20easily%20than%20if%20they%20were%20separate%20processes.
#Modifié par Nolann

#Importation
try:
        import sys
        import random
        import math
        import os
        import getopt
        import pygame
        import threading

        from deplacementCube import *
        
        from socket import *
        from pygame.locals import *
except ImportError as err:
        print("Impossible de charger le module. %s" % (err))
        sys.exit(2)

#Taille de l'écran
ScreenHeight = 720
ScreenWidth = 1280

#Définition d'un Thread
class myThread (threading.Thread):
    
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        
    def run(self):
        print("Starting " + self.name)
        deplacerCube(ScreenWidth, ScreenHeight, 20, 20 , 10)
        print("Exiting " + self.name)

#Création d'un thread
thread1 = myThread(1, "DeplacerCube-1")


#Fonction principale
def main():
    #Fenêtre d'affichage
    pygame.init()
    ecran = pygame.display.set_mode((ScreenWidth,ScreenHeight)) #Taille de la fenêtre
    pygame.display.set_caption('Récupérer un objet') #Nom de la fenêtre

    #Arrière-plan
    background = pygame.Surface(ecran.get_size()) #Taille de l'arrière-plan
    background = background.convert() #Format de l'arrière-plan (équivalent à display)
    background.fill((0, 12, 0)) #Couleur de l'arrière-plan

    #Afficher un texte
    font = pygame.font.Font(None, 36)
    text = font.render("Quitter la fenêtre avec Q", 1, (255,255,255)) #render(Texte,Antialiasing,color,background=None)
    textpos = text.get_rect() #Rentre le texte (texte) dans un rectangle (image)
    textpos.centerx = background.get_rect().centerx #Centre le rectangle en X
    textpos.centery = background.get_rect().centery #Centre le rectangle en Y
    background.blit(text, textpos) #Convertit le texte en image et met en avant le texte par rapport à textpos

    
    #Afficher dans la fenêtre (1re fois)
    ecran.blit(background, (0, 0))
    pygame.display.flip() #Rafraîchit la fenêtre
    
    #Évènements
    
    '''En cours...'''
    
    while 1:
        #Fermer la fenêtre
        for event in pygame.event.get():
            pygame.init()
            if pygame.key.get_pressed()[pygame.K_q]:
                pygame.quit()
                return

        deplacerCube(ScreenWidth, ScreenHeight, 20, 20, 10) #SPAM TEST (lel)
        '''
        Poser la question :
        Comment faire pour multi-threader le déplacement du cube et la récolte des cercles ?
        '''
        
        #Rafraîchit la fenêtre
        ecran.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__':
    main()
