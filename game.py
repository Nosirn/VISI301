import pygame
import pytmx
import pyscroll
import math

from bullet import Bullet
from player import Player
from enemies import Enemy


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
        self.bullet = Bullet(50, 50)

        # var for bullet movement

        self.px = 0
        self.py = 0
        self.radians = 0
        self.dx = 0
        self.dy = 0

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

        if pressed[pygame.K_UP]:
            self.player.move_up()
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
        elif pygame.mouse.get_pressed()[0]:
            if self.bullet.bullet_state == "ready":
                self.px, self.py = pygame.mouse.get_pos()
                #print(self.px, self.py)
                #print(self.group)
                #print(self.player.get_position()[0], self.player.get_position()[1])
                self.fire_bullet(self.player.get_position()[0], self.player.get_position()[1])

    def fire_bullet(self, x, y):
        self.bullet.bullet_state = "fire"
        self.group.add(self.bullet)
        self.bullet.position = [x, y]
        #print(self.bullet.bullet_state)
        #angle de la droite (clic player)
        self.radians = math.atan2(self.py - self.player.get_position()[1], self.px - self.player.get_position()[0])
        self.dx = math.cos(self.radians)
        self.dy = math.sin(self.radians)
        #print(math.cos(self.radians))
        #print(math.sin(self.radians))

    def bullet_movement(self):
        if self.bullet.bullet_state == "fire":
            if self.bullet.position[0] < 200 or self.bullet.position[0] > 600 or self.bullet.position[1] < 200 or self.bullet.position[1] > 600:
                self.bullet.bullet_state = "ready"
                self.group.remove(self.bullet)
                print(self.group)
            else:
                #self.bullet.position += [self.dx, self.dy]     #problème de changement de position
                pass

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
            self.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)



            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()
