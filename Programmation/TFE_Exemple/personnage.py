import pygame
from config import WIDTH,HEIGHT

class Personnage:

    def __init__(self, posX, posY, width, height) :
        self.position = {"x" : posX, "y" : posY}
        self.dimension = {"w" : width, "h" : height}

        image = pygame.image.load("TFE_Exemple/images/freddy_fazbear.png")
        self.image = pygame.transform.scale(image, (self.dimension['w'],self.dimension['h']))
        self.speed = 3
        self.direction = {"right" : False, "left" : False, "up" : False, "down" : False}

    def get(self):
        rectangle = pygame.Rect(self.position['x'], self.position['y'], self.dimension['w'], self.dimension['h'])
        return rectangle
    
    def move(self) :
        if self.position['x'] < 0:
            self.position['x'] += self.speed
        elif self.position['x'] > WIDTH - 600:
            self.position['x'] -= self.speed
        elif self.position['y'] < 10:
            self.position['y'] += self.speed
        elif self.position['y'] > HEIGHT - 170:
            self.position['y'] -= self.speed
        else:
            if self.direction["left"] : 
                self.position['x'] -= self.speed
            if self.direction["right"] : 
                self.position['x'] += self.speed

            if self.direction["up"] : 
                self.position['y'] -= self.speed
            if self.direction["down"] : 
                self.position['y'] += self.speed