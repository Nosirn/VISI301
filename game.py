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
        if pressed[pygame.K_DOWN]:
            self.player.move_down()
        if pressed[pygame.K_LEFT]:
            self.player.move_left()
        if pressed[pygame.K_RIGHT]:
            self.player.move_right()
        if pygame.mouse.get_pressed()[0]:
            if self.bullet.bullet_state == "ready":
                self.px, self.py = pygame.mouse.get_pos()
                #print(self.px, self.py)
                #print(self.group)
                #print(self.player.get_position()[0], self.player.get_position()[1])
                self.fire_bullet(self.player.get_position()[0], self.player.get_position()[1])
# à mettre dans le fichier bullet
    def fire_bullet(self, x, y):
        self.bullet.bullet_state = "fire"

        # angle de la droite (clic player)
        self.radians = math.atan2(self.py - self.player.get_position()[1], self.px - self.player.get_position()[0])
        self.dx = math.cos(self.radians)
        self.dy = math.sin(self.radians)
        print(math.cos(self.radians))
        print(round(math.cos(self.radians)))
        print(math.sin(self.radians))
        print(round(math.sin(self.radians)))

        self.bullet.image = pygame.transform.rotate(self.bullet.image, self.radians)
        self.bullet.position = [x, y]
        self.group.add(self.bullet)
        print(self.bullet.bullet_state)

    def bullet_movement(self):
        if self.bullet.bullet_state == "fire":
            if self.bullet.position[0] < 0 or self.bullet.position[0] > 800 or self.bullet.position[1] < 0 or self.bullet.position[1] > 800:
                self.bullet.bullet_state = "ready"
                self.group.remove(self.bullet)
                print(self.group)
                print(self.bullet.bullet_state)
            else:
                if round(self.dx) == 1:
                    self.bullet.move_right()
                    print("d")
                if round(self.dx) == -1:
                    self.bullet.move_left()
                    print("g")
                if round(self.dy) == 1:
                    self.bullet.move_down()
                    print("h")
                if round(self.dy) == -1:
                    self.bullet.move_up()
                    print("b")

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

    def zombie_touche(self):
        #on prend les coordonnees de la balle et du zombie, si c'est les mêmes, le zombie est touché

        #ne marche pas, renvoit toujours false, il faut essayer en mettant une 'hitbox' sur le sprite en faisant un pygame.rect

        touche = True
        Xzomb = self.enemy.get_position()[0]
        Yzomb = self.enemy.get_position()[1]

        Xbullet = self.bullet.get_position()[0]
        Ybullet = self.bullet.get_position()[1]

        if Xzomb == Xbullet and Yzomb == Ybullet :
            touche = True

        print(touche)

        return touche


    def disparition_sprite(self):
        #permet de faire disparaitre les sprites sous certaines conditions
        if self.zombie_touche() :
            self.group.remove(self.bullet)
            self.group.remove(self.enemy)

        if self.bullet.position[0] < 0 or self.bullet.position[0] > 800 or self.bullet.position[1] < 0 or self.bullet.position[1] > 800:
            self.group.remove(self.bullet)

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
            self.zombie_touche()
            self.disparition_sprite()

            self.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)



            # update the full display surface to the screen
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            #nombre de FPS
            clock.tick(60)

        pygame.quit()
