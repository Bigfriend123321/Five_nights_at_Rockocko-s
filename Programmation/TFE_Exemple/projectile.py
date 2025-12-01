import pygame
from config import WIDTH,HEIGHT,ecran

class Projectile:

    def __init__(self, posX, posY, width, height) :
        self.position = {"x" : posX, "y" : posY}
        self.dimension = {"w" : width, "h" : height}

        image = pygame.image.load("TFE_Exemple/images/heart.png")
        self.image = pygame.transform.scale(image, (self.dimension['w'],self.dimension['h']))
        self.speed = 3
        self.degat = 1
        self.direction = {"right" : False}


    def get(self,background):
        return pygame.Rect(self.position['x'], self.position['y'], self.dimension['w'], self.dimension['h'])

    
    def move(self,background) :
        if self.direction["right"] : 
            self.position['x'] += self.speed