import pygame

from Tanks.Bullets import Bullet
from Tanks.Tanks import TankInterface


class Enemy(TankInterface):

    def __init__(self, position_y, position_x, health, enemy_img):
        self.enemy_img = enemy_img
        self.position_y = position_y
        self.position_x = position_x
        self.health = health
        self.velocity = 5
        self.character_img = pygame.transform.scale(enemy_img, (60, 70))
        self.can_move = True
        self.hitbox = (self.position_y + 20, self.position_x, 28, 60)

    def redraw(self, screen):
        """putting character in the screen with position(x, y)"""
        screen.blit(self.character_img, (self.position_y, self.position_x))
        self.hitbox = (self.position_y + 10, self.position_x + 11, 40, 52)
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def movement(self):
        if self.position_y < 260:
            self.can_move = True

        elif self.position_y > 375:
            self.can_move = False

        """moving left increasing x position if he can move right or decreasing x position if he cant move left"""
        if self.can_move:
            self.position_y += self.velocity
        else:
            self.position_y -= self.velocity

