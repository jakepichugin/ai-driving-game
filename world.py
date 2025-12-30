import math
import pygame
import os
pygame.init()

class Background:
    def __init__(self, screen):
        self.screen = screen
        self.raw_image = pygame.image.load("background.jpg").convert()


        self.background = pygame.transform.scale(self.raw_image, (self.raw_image.get_rect().width * 10, self.raw_image.get_rect().height * 10))
        self.background_rect = self.background.get_rect()
    # def transform(self):

    def draw(self, camera_x, camera_y):
        self.screen.blit(self.background, (0 - camera_x, 0 - camera_y))