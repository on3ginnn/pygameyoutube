__all__ = []

import sys

import pygame


TIFFANY = (129, 216, 208)
PURPLE = (129, 116, 208)
TITLE = "fff"
FAVICON = "static/img/fav/icon.svg"
BACKGROUND_IMAGE = "static/img/bg.jpg"
SPACESHEEP_SPRITE = "static/img/spacesheep2.png"
SIZE = width, height = 960, 720


def terminate():
    pygame.quit()
    sys.exit()


def main():
    bg_y = 0
    bg_speed = 2
    bg = pygame.image.load(BACKGROUND_IMAGE)
    spacesheep_x = (width // 2) - 55
    spacesheep_speed = 2
    spacesheep = pygame.image.load(SPACESHEEP_SPRITE)

    while True:
        screen.blit(bg, (0, bg_y))
        screen.blit(bg, (0, bg_y - height))

        screen.blit(spacesheep, (spacesheep_x, 500))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and spacesheep_x - spacesheep_speed >= 0:
            spacesheep_x -= spacesheep_speed

        if (
            keys[pygame.K_RIGHT]
            and spacesheep_x + spacesheep_speed <= width - 110
        ):
            spacesheep_x += spacesheep_speed

        spacesheep_x %= width - 110

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

        bg_y += bg_speed
        bg_y %= height

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    screen.fill(TIFFANY)
    pygame.display.set_caption(TITLE)
    favicon = pygame.image.load(FAVICON)
    pygame.display.set_icon(favicon)

    clock = pygame.time.Clock()

    main()
