import torch
import torch.nn as nn #accessing neural network base class from torch library (writing nn instead of torch.nn)
import torch.optim as optim # manage gradient descendent and back propagation steps by automation
import numpy as np
import math
import pygame
import main
pygame.init()

STRAIGHT = 0
LEFT = 40
RIGHT = -40




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
        self.turn_direction = STRAIGHT

        self.temp_car_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.car_surface = self.temp_car_surface
        self.car_surface.fill((0, 255, 0))
        self.car_rect = self.car_surface.get_rect()

        #left wheel then right wheel, then left back, then right back
        self.wheels = [Wheel(self.xPos, self.yPos, True, True),
                       Wheel(self.xPos, self.yPos, True, False),
                       Wheel(self.xPos, self.yPos, False, True),
                       Wheel(self.xPos, self.yPos, False, False)]



    def move(self):
        #inputs from keyboard
        keys = pygame.key.get_pressed()

        #input detection
        if keys[pygame.K_LEFT]:
            self.turn_direction = LEFT
        elif keys[pygame.K_RIGHT]:
            self.turn_direction = RIGHT
        else:
            self.turn_direction = STRAIGHT

        if self.speed != 0:
            if keys[pygame.K_LEFT]:
                #turning speed depends on speed
                self.angle += (0.8 * self.speed) / (1 + (abs(1.2 * self.speed) * 0.2))
            if keys[pygame.K_RIGHT]:
                # turning speed depends on speed
                self.angle -= (0.8 * self.speed) / (1 + (abs(1.2 * self.speed) * 0.2))


        #gas and brake keys
        if keys[pygame.K_UP]:
            if self.speed < 10:
                self.speed += 0.2
        if keys[pygame.K_DOWN]:
            if self.speed > -5:
                self.speed -= 0.2

        # friction:
        if self.speed > 0:
            self.speed -= 0.1
        elif self.speed < 0:
            self.speed += 0.1
        if self.speed < 0.1 and self.speed > -0.1:
            self.speed = 0

        # turing wheels:



    def transform(self):
        if self.speed != 0:
            self.car_surface = pygame.transform.rotate(self.temp_car_surface, self.angle)


        self.car_rect = self.car_surface.get_rect()


        radian = math.radians(self.angle + 90)
        self.xVel = self.speed * math.cos(radian)
        self.yVel = self.speed * math.sin(radian)

        self.xPos += self.xVel
        self.yPos -= self.yVel

        pivot = pygame.math.Vector2(self.xPos, self.yPos)
        offset = pygame.math.Vector2(0, -self.height / 2)
        rotated_offset = offset.rotate(-self.angle)
        self.car_rect.center = (int((pivot + rotated_offset).x), int((pivot + rotated_offset).y))

        self.car_rect.clamp_ip(main.screen.get_rect())

        print(f"Angle: {self.angle} , Speed: {self.speed}, xVel: {self.xVel}, yVel: {self.yVel}")

class Wheel:
    def __init__(self, xpos, ypos, frontWheel, leftWheel):
        self.width = 10
        self.height = 20
        self.xPos = xpos
        self.yPos = ypos
        self.angle = 0
        self.is_front_wheel = frontWheel
        self.is_left_wheel = leftWheel
        self.temp_wheel_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.wheel_surface = self.temp_wheel_surface
        self.wheel_surface.fill((100, 100, 100))
        self.wheel_rect = self.wheel_surface.get_rect()

    def turn(self, car):

        if self.is_front_wheel:
            self.wheel_surface = pygame.transform.rotate(self.temp_wheel_surface, car.angle + car.turn_direction)
        if not self.is_front_wheel:
            self.wheel_surface = pygame.transform.rotate(self.temp_wheel_surface, car.angle)
        self.wheel_rect = self.wheel_surface.get_rect()

        side_dist = -25 if self.is_left_wheel else 25
        front_dist = -car.height + self.height if self.is_front_wheel else -self.height

        wheel_offset = pygame.math.Vector2(side_dist, front_dist)
        rotated_wheel_pos = wheel_offset.rotate(-car.angle)

        self.wheel_rect.center = (int((car.xPos + rotated_wheel_pos.x)), int((car.yPos + rotated_wheel_pos.y)))
