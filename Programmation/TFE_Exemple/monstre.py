import pygame
import pygame
from config import WIDTH,HEIGHT
from random import randrange
from time import time

class Monstre:
    def __init__(self, posX, posY, boss=False) :
        self.position = {"x" : posX, "y" : posY}

        if boss :
            self.dimension = {"w" : 100, "h" : 100}
            image = pygame.image.load("TFE_Exemple/images/crying_child.png")
            self.vie = 30
            self.speed = 2
            self.boss = True

        else :
            self.dimension = {"w" : 50, "h" : 50}
            image = pygame.image.load("TFE_Exemple/images/crying_child.png")
            self.vie = 3
            self.speed = 4
            self.boss = False
        self.time_lastMove = 0
        self.time_lastMovement = 0
        self.image = pygame.transform.scale(image, (self.dimension['w'],self.dimension['h']))
        self.direction = {"right" : False, "left" : False, "up" : False, "down" : False}

    def move(self) :
        movement = ['right', 'left', 'up', 'down']
        if self.position['x'] < 470:
            self.position['x'] += self.speed
        elif self.position['x'] > WIDTH - 70:
            self.position['x'] -= self.speed
        elif self.position['y'] < 30:
            self.position['y'] += self.speed
        elif self.position['y'] > HEIGHT - 70:
            self.position['y'] -= self.speed
        else:
            if time() - self.time_lastMove > 0.2:
                time_total = 0
                i = 0
                sense = movement[randrange(0,4)]
                if self.boss : 
                    if sense == 'left' : 
                            self.position['x'] -= self.speed
                    if sense == 'right' : 
                            self.position['x'] += self.speed
                            i += 1

                    if sense == 'up' : 
                            self.position['y'] -= self.speed
                    if sense == 'down' : 
                            self.position['y'] += self.speed
                else : 
                    if sense == 'left' : 
                        while i < 10:
                            self.position['x'] -= self.speed
                            i += 1
                    if sense == 'right' : 
                        while i < 10:
                            self.position['x'] += self.speed
                            i += 1

                    if sense == 'up' : 
                        while i < 10:
                            self.position['y'] -= self.speed
                            i += 1
                    if sense == 'down' : 
                        while i < 10:
                            self.position['y'] += self.speed
                            i += 1
                self.time_lastMove = time()

    def get(self) : 
        rectangle = pygame.Rect(self.position['x'],self.position['y'],self.dimension['w'],self.dimension['h'])
        return rectangle