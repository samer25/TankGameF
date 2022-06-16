import pygame
from Tanks.Tanks import TankInterface


class Player(TankInterface):
    def __init__(self, position_y, position_x, health, player_img):
        self.player_img = player_img
        self.position_y = position_y
        self.position_x = position_x
        self.health = health
        self.velocity = 5
        self.character_img = pygame.transform.scale(self.player_img, (60, 70))
        self.hitbox = (self.position_y + 20, self.position_x, 28, 60)

    def redraw(self, screen):
        """putting character in the screen with position(x, y)"""
        screen.blit(self.character_img, (self.position_y, self.position_x))
        self.hitbox = (self.position_y + 17, self.position_x + 11, 29, 52)
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def health_bar(self, screen):
        pass
        # pygame.draw.rect(screen, (0, 128, 0),
        #                  (self.position_x + 7, self.position_y + 80,
        #                   self.health_percent, 10))

