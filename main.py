import pygame as pygame

from BackGround.game_load import redraw_game_window
from Tanks.Bullets import Bullet
from Tanks.Enemy import Enemy
from Tanks.Player import Player

"""Set up Player"""
player_img = pygame.image.load('media/tanks/character.png')
player_position_y = 325
player_position_x = 560
player_health = 100
player = Player(player_position_y, player_position_x, player_health, player_img)

"""Set up Enemy"""
enemy_img = pygame.image.load('media/tanks/enemy_tank.png')
enemy_position_y = 325
enemy_position_x = 70
enemy_health = 100
enemy = Enemy(enemy_position_y, enemy_position_x, enemy_health, enemy_img)


def game_run():
    next_level = 0
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Tank Game")
    run = True
    bullets = []
    e_bullets = []
    while run:
        redraw_game_window(screen, next_level)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        """PLAYER"""
        player.redraw(screen)

        if keys[pygame.K_LEFT] and player.position_y > 260:
            player.position_y -= player.velocity

        if keys[pygame.K_RIGHT] and player.position_y < 375:
            player.position_y += player.velocity

        """Bullets"""
        for bullet in bullets:
            if bullet.y > -20:
                bullet.y -= bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
            """Bullet collision with enemy"""
            if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[
                1]:  # Checks x coords
                if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + \
                        enemy.hitbox[2]:  # Checks y coords
                    enemy.hit()  # calls enemy hit method
                    bullets.pop(bullets.index(bullet))  # removes bullet from bullet list

        if keys[pygame.K_SPACE]:
            if len(bullets) < 1:
                bullets.append(
                    Bullet(round(player.position_y + 60 // 2), round(player.position_x + 70 // 2), 6, (0, 0, 0)))
        for bullet in bullets:
            bullet.draw(screen)

        """ENEMY"""
        enemy.redraw(screen)
        enemy.movement()
        """Enemy Bullets"""
        for bullet in e_bullets:
            if bullet.y < 800:
                bullet.y += bullet.vel
            else:
                e_bullets.pop(e_bullets.index(bullet))

            """Bullet collision with player"""
            if bullet.y - bullet.radius < player.hitbox[1] + player.hitbox[3] and bullet.y + bullet.radius > \
                    player.hitbox[
                        1]:  # Checks x coords
                if bullet.x + bullet.radius > player.hitbox[0] and bullet.x - bullet.radius < player.hitbox[0] + \
                        player.hitbox[2]:  # Checks y coords
                    player.hit()  # calls enemy hit method
                    e_bullets.pop(e_bullets.index(bullet))  # removes bullet from bullet list

        if len(e_bullets) < 1:
            e_bullets.append(
                Bullet(round(enemy.position_y + 60 // 2), round(enemy.position_x + 70 // 2), 6, (0, 0, 0)))
        for bullet in e_bullets:
            bullet.draw(screen)

        """Updating Display"""
        pygame.display.update()

        """fps"""
        clock.tick(27)
    pygame.quit()


if __name__ == '__main__':
    game_run()
