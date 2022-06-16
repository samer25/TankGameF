import pygame


def redraw_game_window(screen, next_level):
    background_images = (
        'media/background/bg.png',
        'media/background/bg2.png',
        "media/background/bg3.png",
        "media/background/bg4.png",
        "media/background/bg5.png",
        "media/background/bg6.png",
        "media/background/bg7.png",
        "media/background/bg8.png",
        "media/background/bg9.png",
        "media/background/bg10.png",
        "media/background/bg11.png",
        "media/background/bg12.png",
        "media/background/bg13.png",
        "media/background/bg14.png",
        "media/background/bg15.png",
        'media/background/bg2.png',
        'media/background/bg4.png',
        "media/background/bg5.png",
        "media/background/bg1.png")

    """setting background in the screen at position x y"""
    """loading image"""
    background_images_load = pygame.image.load(background_images[next_level])
    """scaling the size of image"""
    background_set = pygame.transform.scale(background_images_load, (700, 700))

    screen.blit(background_set, (0, 0))
