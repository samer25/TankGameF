import pygame


class Bullet(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 8
        self.bullets = []

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

