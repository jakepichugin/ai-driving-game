import torch
import torch.nn as nn #accessing neural network base class from torch library (writing nn instead of torch.nn)
import torch.optim as optim # manage gradient descendent and back propagation steps by automation
import numpy as np
import math
import pygame
import main
pygame.init()

STRAIGHT = 40
LEFT = 0
RIGHT = 80
class Car:
    def __init__(self):
        self.width = 50
        self.height = 100
        self.xPos = 800
        self.yPos = 800
        self.angle = 0
        self.speed = 0.0
        self.xVel = 0.0
        self.yVel = 0.0
        self.turnSpeed = 0.0
        self.turnDirection = STRAIGHT

        self.temp_car_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.car_surface = self.temp_car_surface
        self.car_surface.fill((0, 255, 0))
        self.car_rect = self.car_surface.get_rect()

    def move(self):
        keys = pygame.key.get_pressed()
        if self.speed != 0:
            if keys[pygame.K_LEFT]:
                self.turnDirection = LEFT
                self.angle += (0.8 * self.speed) / (1 + (abs(1.2 * self.speed) * 0.2))
            if keys[pygame.K_RIGHT]:
                self.turnDirection = RIGHT
                self.angle -= (0.8 * self.speed) / (1 + (abs(1.2 * self.speed) * 0.2))
        else:
            self.turnDirection = STRAIGHT

        if keys[pygame.K_UP]:
            if self.speed < 10:
                self.speed += 0.5
        if keys[pygame.K_DOWN]:
            if self.speed > -10:
                self.speed -= 0.5

        # friction:
        if self.speed > 0:
            self.speed -= 0.1
        elif self.speed < 0:
            self.speed += 0.1

        if self.speed < 0.1 and self.speed > -0.1:
            self.speed = 0


    def transform(self):
        if self.speed != 0 and self.turnDirection != STRAIGHT:
            self.car_surface = pygame.transform.rotate(self.temp_car_surface, self.angle)

        self.car_rect = self.car_surface.get_rect()

        radian = math.radians(self.angle + 90)
        self.xVel = self.speed * math.cos(radian)
        self.yVel = self.speed * math.sin(radian)

        self.xPos += self.xVel
        self.yPos -= self.yVel

        self.car_rect.center = (self.xPos, self.yPos)

        self.car_rect.clamp_ip(main.screen.get_rect())

        print(f"Angle: {self.angle} , Speed: {self.speed}, xVel: {self.xVel}, yVel: {self.yVel}")

