import torch
import torch.nn as nn #accessing neural network base class from torch library (writing nn instead of torch.nn)
import torch.optim as optim # manage gradient descendent and back propagation steps by automation
import numpy as np
import pygame
import car
from car import Car
from world import Background

screen = pygame.display.set_mode((1800, 1200))
clock = pygame.time.Clock()

background = Background(screen)
player = Car(screen)
bot = Car(screen)

#camera_x/y is the distance of the player from the center of the screen
camera_x = player.xPos - (screen.get_width()/2)
camera_y = player.yPos - (screen.get_height()/2)

def draw():
    screen.fill((0, 0, 0))

    background.draw(camera_x, camera_y)
    for wheel in player.wheels:
        wheel.draw(camera_x, camera_y)
    player.draw(camera_x, camera_y)
    pygame.display.flip()




running = True
while running:
    camera_x = player.xPos - (screen.get_width() / 2)
    camera_y = player.yPos - (screen.get_height() / 2)
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
