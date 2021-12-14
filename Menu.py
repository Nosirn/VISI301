#Par Nolann

import pygame
import pygame_menu

pygame.init()

screenDim = (800,800) # Taille de l'écran
screen = pygame.display.set_mode(screenDim)

def Menu(choix, surface):
    if choix == "principal":
        principal.mainloop(surface)
    elif choix == "mort":
        mort.mainloop(surface)
    elif choix == "options":
        options.mainloop(surface)
    else:
        print("Le choix désiré n'existe pas.")

## Promo autres groupes
secret = pygame_menu.Menu("Les jeux des CMI",screenDim[0],screenDim[1], theme=pygame_menu.themes.THEME_GREEN)
path_groupe1 = "groupe1.png"
path_groupe2 = "groupe2.png"
secret.add.image(path_groupe1, scale=(screenDim[0]/1280*0.5,screenDim[1]/720*0.5))
secret.add.image(path_groupe2, scale=(screenDim[0]/1280*0.5,screenDim[1]/720*0.5))
## manque un moyen de quitter (W.I.P.)

## Menu des options
options = pygame_menu.Menu("Options",screenDim[0],screenDim[1], theme=pygame_menu.themes.THEME_GREEN)
options.add.range_slider('Musique',50, (0, 100), 1, rangeslider_id="music", value_format=lambda x: str(int(x)))
options.add.range_slider('Effets sonore',50, (0, 100), 1, rangeslider_id="sfx", value_format=lambda x: str(int(x)))
## manque un moyen de quitter (W.I.P.)

## Menu principal
principal = pygame_menu.Menu("Bienvenue !",screenDim[0],screenDim[1], theme=pygame_menu.themes.THEME_BLUE)
principal.add.text_input('Nom du Perso : ', default='Billy')
principal.add.button('Lancer la partie') #Ajouter le lancement de partie
principal.add.button('Quitter le jeu', pygame_menu.events.EXIT) #Quitter


mort = pygame_menu.Menu("Vous êtes mort D:",screenDim[0],screenDim[1], theme=pygame_menu.themes.THEME_DARK)
mort.add.button('Relancer une partie') #Ajouter l'option pour relancer une partie ? ('...', Fonction)
mort.add.button('Quitter le jeu', pygame_menu.events.EXIT)

if __name__ == '__main__':
    Menu('principal', screen)
