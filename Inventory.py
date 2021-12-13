import pygame
from InventorySlot import InventorySlot

class Inventory:
    def __init__(self):
        self.slots = []
        self.image = pygame.image.load("images/inventorybar.png")
        self.rect = self.image.get_rect()
        self.rect.topleft= (570, 710)

        self.slots.append(InventorySlot("images/coin.png",(580, 723)))



    def render(self, screen):
        screen.blit(self.image, self.rect)
        for slot in self.slots:
            slot.render(screen)
