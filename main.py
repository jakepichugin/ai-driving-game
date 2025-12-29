import torch
import torch.nn as nn #accessing neural network base class from torch library (writing nn instead of torch.nn)
import torch.optim as optim # manage gradient descendent and back propagation steps by automation
import numpy as np
import pygame
from car import Car
from car import Wheel

player = Car()

screen = pygame.display.set_mode((1800, 1200))

clock = pygame.time.Clock()
def draw():
    screen.fill((0, 0, 0))

    for wheel in player.wheels:
        screen.blit(wheel.wheel_surface, wheel.wheel_rect)
    screen.blit(player.car_surface, player.car_rect)
    pygame.display.flip()




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move()
    player.transform()
    for wheel in player.wheels:
        wheel.turn(player)
    draw()
    screen.fill((0,0,0))
    clock.tick(60)

pygame.quit()
