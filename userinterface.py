import pygame
from Inventory import Inventory
from Score import Score


class UserInterface:
    def __init__(self, mun, coin, smg_mag, pistol_mag, vague):
        self.color_red = (255, 0, 0)
        self.color_green = (0, 255, 0)
        self.color_blue = (0, 0, 255)
        self.color_black = (0, 0, 0)
        self.color_white = (255, 255, 255)

        self.smallfont = pygame.font.SysFont("Verdana", 12)
        self.regularfont = pygame.font.SysFont("Verdana", 20)
        self.largefont = pygame.font.SysFont("Verdana", 40)

        self.inventory = Inventory(mun, coin, smg_mag, pistol_mag)
        #self.inventoryRender = True

        self.text = self.regularfont.render("point : ", True, self.color_black)
        self.score = self.regularfont.render("0", True, self.color_black)
        self.vague = self.regularfont.render(str("vague :"), True, self.color_black)
        self.num_vague = self.regularfont.render(str(vague-1), True, self.color_black)

    def render(self, screen):
        #if self.inventoryRender == True:
        self.inventory.render(screen)
        screen.blit(self.text, (660, 15))
        screen.blit(self.score, (740, 15))
        screen.blit(self.vague, (660, 45))
        screen.blit(self.num_vague, (740, 45))

    def update(self, mun, coin, point,smg_mag, pistol_mag, vague):
        self.inventory = Inventory(mun, coin, smg_mag, pistol_mag)
        new_point = point
        self.text = self.regularfont.render(str("point :"), True, self.color_black)
        self.score = self.regularfont.render(str(point), True, self.color_black)
        self.vague = self.regularfont.render(str("vague :"), True, self.color_black)
        self.num_vague = self.regularfont.render(str(vague-1), True, self.color_black)
    
    # def toggleInventory(self):
    #     if self.inventoryRender == True:
    #         self.inventoryRender = False
    #     elif self.inventoryRender == False:
    #         self.inventoryRender = True


