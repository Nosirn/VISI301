import pygame
import pytmx
import pyscroll
import math

from bullet import Bullet
from player import Player
from enemies import Enemy
from pieces import Piece


class Game:

    def __init__(self):

        # initialize the pygame
        pygame.init()

        # create the screen
        self.screen = pygame.display.set_mode((800, 800))

        # Title and icon
        pygame.display.set_caption("CMI-zombie")
        icon = pygame.image.load('images/zombie.png')
        pygame.display.set_icon(icon)

        # map charge
        tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        # map_layer.zoom = 2

        # generate player
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        # generate enemy
        enemy_position = tmx_data.get_object_by_name("spawn_zombie1")  # Faire spawn aléatoirement
        self.enemy = Enemy(enemy_position.x, enemy_position.y)

        # generate bullet
        self.bullet = Bullet(self.player.get_position()[0], self.player.get_position()[1])

        #generate Piece
        self.piece = Piece(0, 0)

        # var for bullet movement

        # self.px = 0
        # self.py = 0
        # self.radians = 0
        # self.dx = 0
        # self.dy = 0

        # Collision

        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=4)
        self.group.add(self.player)
        self.group.add(self.enemy)

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
            if self.bullet.bullet_state == "ready":
                self.px, self.py = pygame.mouse.get_pos()
                self.fire_bullet()

    def fire_bullet(self):

        # On place la balle sur le joueur et on la fait apparaitre
        self.bullet.position = [self.player.position[0], self.player.position[1]]
        self.bullet.bullet_state = "fire"  # On passe l'état du tir à fires
        self.vector = self.vector_bullet()  # on recupère le vecteur de direction du tir
        self.group.add(self.bullet)

        # on reduit le vecteur au maximum
        if abs(self.vector[0]) > abs(self.vector[1]):
            i = abs(self.vector[0])
        else:
            i = abs(self.vector[1])

        self.vector = [self.vector[0] / i, self.vector[1] / i]
        print(self.vector)

    # à mettre dans le fichier bullet
    def vector_bullet(self):

        # On recupère la position de la balle
        posBulletX = self.bullet.position[0]
        posBulletY = self.bullet.position[1]

        # On recupère les coordonées du clic
        posMouseX = pygame.mouse.get_pos()[0]
        posMouseY = pygame.mouse.get_pos()[1]

        # On calcul le vecteur de direction de la balle
        vect = [posMouseX - posBulletX, posMouseY - posBulletY]

        print(vect)
        return vect

    def bullet_movement(self):

        bulletspeed = 6

        if self.bullet.bullet_state == "fire":
            pX = self.bullet.position[0]
            # print(self.bullet.position[0])
            pY = self.bullet.position[1]
            # print(self.bullet.position[1])

            pX += bulletspeed * self.vector[0]
            pY += bulletspeed * self.vector[1]

            self.bullet.position = [pX, pY]

    def follow_player(self):

        if self.enemy.get_position()[0] > self.player.get_position()[0]:
            self.enemy.move_left()
        elif self.enemy.get_position()[0] < self.player.get_position()[0]:
            self.enemy.move_right()
        if self.enemy.get_position()[1] > self.player.get_position()[1]:
            self.enemy.move_up()
        elif self.enemy.get_position()[1] < self.player.get_position()[1]:
            self.enemy.move_down()

        self.enemy.position[0] += self.enemy.change_position[0]
        self.enemy.position[1] += self.enemy.change_position[1]
        self.enemy.change_position = [0, 0]

    def zombie_touche(self):
        # on prend les coordonnees de la balle et du zombie, si c'est les mêmes, le zombie est touché

        touche = False
        # renvoie 1 si les deux sprite en parametre se touche
        if pygame.sprite.collide_rect(self.bullet, self.enemy) == 1 and self.bullet in self.group:
            touche = True

        return touche

    #def spawn_piece(self):
        #self.group.add(self.piece)

    def disparition_sprite(self):
        # permet de faire disparaitre les sprites sous certaines conditions

        if self.zombie_touche():
            self.group.remove(self.bullet)
            self.bullet.bullet_state = "ready"
            self.group.remove(self.enemy)
            #self.spawn_piece()

        if self.bullet.position[0] < 0 or self.bullet.position[0] > 800 or self.bullet.position[1] < 0 or \
                self.bullet.position[1] > 800:
            self.group.remove(self.bullet)
            self.bullet.bullet_state = "ready"

    def update(self):
        self.group.update()

        # Test collision
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

    def run(self):
        clock = pygame.time.Clock()

        # Game loop
        running = True
        while running:

            self.follow_player()
            self.enemy.save_location()
            self.player.save_location()
            self.bullet.save_location()
            self.handle_input()
            self.bullet_movement()
            self.disparition_sprite()

            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            self.update()

            # update the full display surface to the screen
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # nombre de FPS
            clock.tick(60)

        pygame.quit()
