import torch
import torch.nn as nn #accessing neural network base class from torch library (writing nn instead of torch.nn)
import torch.optim as optim # manage gradient descendent and back propagation steps by automation
import numpy as np
import pygame
from car import Car

player = Car()

screen = pygame.display.set_mode((1800, 1200))

clock = pygame.time.Clock()
def draw():
    screen.fill((0, 0, 0))
    screen.blit(player.car_surface, player.car_rect)
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move()
    player.transform()

    draw()
    screen.fill((0,0,0))
    clock.tick(60)

pygame.quit()
