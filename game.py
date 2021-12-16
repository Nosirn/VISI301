import pygame
import pytmx
import pyscroll
import math
import random
import pygame_menu
from pygame import mixer


from bullet import Bullet
from player import Player
from enemies import Enemy
from userinterface import UserInterface



class Game:

    def __init__(self):

        # initialize the pygame
        pygame.init()

        # create the screen
        self.screenDim = (800, 800)
        self.screen = pygame.display.set_mode(self.screenDim)

        # Title and icon
        pygame.display.set_caption("CMI-zombie")
        icon = pygame.image.load('images/zombie.png')
        pygame.display.set_icon(icon)

        # map charge
        tmx_data = pytmx.util_pygame.load_pygame('map-interieur.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        # generate player
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        #var

        self.numero_vague = 0
        self.vague_fini = True
        self.wait = "non appuyé"

        # user interface

        self.UI = UserInterface(self.player.munition, self.player.coin, self.player.smg_magazine, self.player.pistol_magazine, self.numero_vague)

        # Collision
        self.bullets = []
        self.zombies = []
        self.walls = []
        self.test = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=4)
        self.group.add(self.player)
        self.bullet_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()



        #######################initialisation Menu################################

        ## Promo autres groupes
        self.secret = pygame_menu.Menu("Les jeux des CMI", self.screenDim[0], self.screenDim[1],
                                  theme=pygame_menu.themes.THEME_GREEN)
        path_groupe1 = "images/groupe1.png"
        path_groupe2 = "images/groupe2.png"
        self.secret.add.image(path_groupe1, scale=(self.screenDim[0] / 1280 * 0.5, self.screenDim[1] / 720 * 0.5))
        self.secret.add.image(path_groupe2, scale=(self.screenDim[0] / 1280 * 0.5, self.screenDim[1] / 720 * 0.5))
        ## manque un moyen de quitter (W.I.P.)

        ## Menu des options
        self.options = pygame_menu.Menu("options", self.screenDim[0], self.screenDim[1], theme=pygame_menu.themes.THEME_GREEN)
        self.options.add.range_slider('Musique', 50, (0, 100), 1, rangeslider_id="music", value_format=lambda x: str(int(x)))
        self.options.add.range_slider('Effets sonore', 50, (0, 100), 1, rangeslider_id="sfx",
                                 value_format=lambda x: str(int(x)))
        self.options.add.button('retour au jeu', self.start)
        self.options.add.button('Quitter le jeu', pygame_menu.events.EXIT)
        ## manque un moyen de quitter (W.I.P.)

        ## Menu des options
        self.options = pygame_menu.Menu("Options", self.screenDim[0], self.screenDim[1],
                                        theme=pygame_menu.themes.THEME_GREEN)
        self.options.add.range_slider('Musique', 50, (0, 100), 1, rangeslider_id="music",
                                      value_format=lambda x: str(int(x)))
        self.options.add.range_slider('Effets sonore', 50, (0, 100), 1, rangeslider_id="sfx",
                                      value_format=lambda x: str(int(x)))
        self.options.add.button('commandes', self.show_control)
        self.options.add.button('retour au jeu', self.start)
        self.options.add.button('Quitter le jeu', pygame_menu.events.EXIT)

        ## Menu des controles
        self.control = pygame_menu.Menu("Commandes", self.screenDim[0], self.screenDim[1],
                                        theme=pygame_menu.themes.THEME_GREEN)
        self.control.add.text_input('haut : ', default='z')
        self.control.add.text_input('bas : ', default='s')
        self.control.add.text_input('gauche : ', default='q')
        self.control.add.text_input('droite : ', default='d')
        self.control.add.text_input('rechargement : ', default='r')
        self.control.add.text_input('acheter des munitions : ', default='c')
        self.control.add.text_input('poing : ', default='1')
        self.control.add.text_input('Pistolet : ', default='2')
        self.control.add.text_input('mitraillette : ', default='3')
        self.control.add.button('retour', self.start)
        self.control.add.button('Quitter le jeu', pygame_menu.events.EXIT)
        ## manque un moyen de quitter (W.I.P.)

        ## Menu principal
        self.principal = pygame_menu.Menu("Bienvenue !", self.screenDim[0], self.screenDim[1],
                                     theme=pygame_menu.themes.THEME_BLUE)
        self.principal.add.text_input('Nom du Perso : ', default='Billy')
        self.principal.add.button('Lancer la partie', self.start)
        self.principal.add.button('commandes', self.show_control)
        self.principal.add.button('Quitter le jeu', pygame_menu.events.EXIT)  # Quitter

        self.mort = pygame_menu.Menu("Vous êtes mort D:", self.screenDim[0], self.screenDim[1],
                                theme=pygame_menu.themes.THEME_DARK)
        #self.mort.add.button('Relancer une partie')  # Ajouter l'option pour relancer une partie ?
        self.mort.add.button('Quitter le jeu', pygame_menu.events.EXIT)


    def show_control(self):
        self.Menu("control", self.screen)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_z]:
            self.player.move_up()
        if pressed[pygame.K_s]:
            self.player.move_down()
        if pressed[pygame.K_q]:
            self.player.move_left()
        if pressed[pygame.K_d]:
            self.player.move_right()
        if pygame.mouse.get_pressed()[0]:
            if self.player.can_shoot():
                self.player.remove_bullet_magazine()
                self.bullet_group.add(self.player.create_bullet())

        if pressed[pygame.K_1]:
            self.player.change_weapon('hand')
            self.player.weapon = self.player.hand()
        if pressed[pygame.K_2]:
            self.player.change_weapon('pistol')
            self.player.weapon = self.player.pistol()
        if pressed[pygame.K_3]:
            self.player.change_weapon('smg')
            self.player.weapon = self.player.smg()
        if pressed[pygame.K_r]:
            self.player.reload()
        if pressed[pygame.K_c]:
            self.wait = "appuyé"
        if self.wait == "appuyé" and not pressed[pygame.K_c]:
            self.player.buy_munition()
            self.wait = "non appuyé"
        if pressed[pygame.K_ESCAPE]:
            self.Menu("options", self.screen)
        #if pressed[pygame.K_x]:
        #   self.UI.toggleInventory()

    def vagues(self, taille_vague):
        for i in range(0, taille_vague):
            if random.randint(0,1) == 0:
                if random.randint(0,1) == 0:
                    self.spawn(random.randint(50,700), 50)
                else:
                    self.spawn(random.randint(50, 700), 700)
            else:
                if random.randint(0,1) == 0:
                    self.spawn(50, random.randint(50,700))
                else:
                    self.spawn(700, random.randint(50,700))

    def spawn(self, x, y):
        self.enemy_group.add(Enemy(x,y))
        self.zombies.append(pygame.Rect(0, 0, 56, 60))

    def new_vague(self):
        if len(self.enemy_group) == 0:
            self.vagues(self.numero_vague)
            self.numero_vague += 1


    def update(self):
        self.group.update()
        self.bullet_group.update()
        self.enemy_group.update(self.player.position[0], self.player.position[1], self.zombies)
        self.UI.update(self.player.munition, self.player.coin, self.player.score, self.player.smg_magazine, self.player.pistol_magazine, self.numero_vague)

        # Gestion collision
        i = 0
        for sprite in self.enemy_group:
            sprite.update_health_bar(self.screen)
            self.zombies[i] = sprite.rect
            i += 1

        for sprite in self.bullet_group.sprites():
            if sprite.rect.collidelist(self.zombies) > -1:
                for zombie in self.enemy_group.sprites():
                    if pygame.sprite.collide_rect(zombie, sprite):
                        zombie.touche()
                        self.zombies.remove(zombie)
                sprite.touche()
                self.player.get_coin()
                self.player.get_point()

        for sprite in self.group.sprites():
            if sprite.rect.collidelist(self.walls) > -1:
                sprite.move_back()
        for sprite in self.enemy_group.sprites():
            if sprite.rect.collidelist(self.walls) > -1:
                sprite.move_back()

    def Menu(self, choix, surface):
        if choix == "principal":
            self.principal.mainloop(surface)
        elif choix == "mort":
            self.mort.mainloop(surface)
        elif choix == "options":
            self.options.mainloop(surface)
        elif choix == "secret":
            self.secret.mainloop(surface)
        elif choix == "control":
            self.control.mainloop(surface)
        else:
            print("Le choix désiré n'existe pas.")

            

    def dammages(self):
        for zombie in self.enemy_group.sprites():
            zombie.tempo()
            if zombie.rect.colliderect(self.player.rect) and zombie.cooldown == 0:
                self.player.health = self.player.health - 1
                zombie.cooldown = 1
                
                print(self.player.health)
            

    def dead(self):
        if self.player.health <= 0:
            living = False
        else :
            living = True
        return living

    def start(self):
        print("lancement de la partie")
        clock = pygame.time.Clock()
        # Game loop
        alive = True
        while alive:

            self.update()
            self.player.save_location()
            for sprite in self.enemy_group:
                sprite.save_location()
            self.handle_input()
            self.group.draw(self.screen)
            self.bullet_group.draw(self.screen)
            self.enemy_group.draw(self.screen)
            self.UI.render(self.screen)
            self.new_vague()
            self.dammages()
            print(self.player.weapon_name)


            # update the full display surface to the screen
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    alive = False

            alive = self.dead()
            # nombre de FPS
            clock.tick(60)

        self.Menu("mort", self.screen)



    def run(self):

        self.Menu('principal', self.screen)
        pygame.quit()
