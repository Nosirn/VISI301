import pygame
import pytmx
import pyscroll
import math
import random

from bullet import Bullet
from player import Player
from enemies import Enemy
from pieces import Piece
from userinterface import UserInterface


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
        #zzmap_layer.zoom = 2

        # generate player
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        # user interface

        self.UI = UserInterface()

        # generate enemy
        enemy_position = tmx_data.get_object_by_name("spawn_zombie1")  # Faire spawn aléatoirement
        self.enemy = Enemy(enemy_position.x, enemy_position.y)

        # generate bullet 
        #self.bullet = Bullet(self.player.get_position()[0], self.player.get_position()[1])
        

        #generate Piece
        self.piece = Piece(0, 0)

        # Collision

        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=4)
        self.group.add(self.player)
        self.bullet_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()

        self.new_vague = True

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
                self.bullet_group.add(self.player.create_bullet())

        if pressed[pygame.K_c]:
            self.player.change_weapon('hand')
            self.player.weapon = self.player.hand()
        if pressed[pygame.K_a]:
            self.player.change_weapon('pistol')
            self.player.weapon = self.player.pistol()
        if pressed[pygame.K_f]:
            self.player.change_weapon('smg')
            self.player.weapon = self.player.smg()
        if pressed[pygame.K_r]:
            self.player.reload()
        #if pressed[pygame.K_x]:
        #   self.UI.toggleInventory()

    def vagues(self, taille_vague):
        for i in range(0, taille_vague):
            self.enemy_group.add(Enemy(random.randint(100, 700), random.randint(100, 700)))

    def update_enemy(self):
        self.enemy_group.update(self.player.position[0], self.player.position[1])


    def update(self):
        self.group.update()
        self.bullet_group.update()
        self.update_enemy()

        # Test collision
        for sprite in self.group.sprites():
            if sprite.rect.collidelist(self.walls) > -1:
                sprite.move_back()

    def run(self):
        clock = pygame.time.Clock()

        # Game loop
        running = True
        while running:
            self.update()
            self.enemy.save_location()
            self.player.save_location()
            self.handle_input()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            self.bullet_group.draw(self.screen)
            self.enemy_group.draw(self.screen)
            self.UI.render(self.screen)
            if self.new_vague == True:
                self.vagues(2)
                self.new_vague = False

            # update the full display surface to the screen
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # nombre de FPS
            clock.tick(60)

        pygame.quit()
