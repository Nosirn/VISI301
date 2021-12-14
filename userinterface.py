import pygame
from Inventory import Inventory


class UserInterface:
    def __init__(self, mun, coin):
        self.color_red = (255, 0, 0)
        self.color_green = (0, 255, 0)
        self.color_blue = (0, 0, 255)
        self.color_black = (0, 0, 0)
        self.color_white = (255, 255, 255)

        self.smallfont = pygame.font.SysFont("Verdana", 12)
        self.regularfont = pygame.font.SysFont("Verdana", 20)
        self.largefont = pygame.font.SysFont("Verdana", 40)

        self.inventory = Inventory(mun, coin)
        #self.inventoryRender = True

        self.text = self.regularfont.render("0", True, self.color_black)


    def render(self, screen):
        #if self.inventoryRender == True:
        self.inventory.render(screen)

    def update(self, mun, coin):
        self.inventory = Inventory(mun, coin)

    # def toggleInventory(self):
    #     if self.inventoryRender == True:
    #         self.inventoryRender = False
    #     elif self.inventoryRender == False:
    #         self.inventoryRender = True


