__all__ = []

import sys

import pygame


TIFFANY = (129, 216, 208)
PURPLE = (129, 116, 208)
TITLE = "fff"
FAVICON = "static/img/fav/icon.svg"
SIZE = width, height = 600, 300


def terminate():
    pygame.quit()
    sys.exit()


def main():
    square = pygame.Surface((100, 100))
    square.fill(PURPLE)

    myfont = pygame.font.Font(
        "static/font/Inconsolata/static/Inconsolata-Regular.ttf", 28
    )
    text = myfont.render(
        "lorem text lorem text lorem text lorem text", True, TIFFANY, PURPLE
    )

    img = pygame.image.load("static/img/content/f.png")

    rect = square.get_rect()
    speed = [2, 2]

    selected = [100, 50, 500, 250]
    mouse_select = False

    x, w = selected[0], selected[2] - selected[0]
    y, h = selected[1], selected[3] - selected[1]
    selected_zone = pygame.Surface((w, h))

    while True:
        screen.fill(TIFFANY)
        screen.blit(text, (0, 0))

        x, w = selected[0], selected[2] - selected[0]
        y, h = selected[1], selected[3] - selected[1]

        if selected[2] < selected[0]:
            x, w = selected[2], selected[0] - selected[2]

        if selected[3] < selected[1]:
            y, h = selected[3], selected[1] - selected[3]

        if mouse_select:
            selected_zone = pygame.Surface((w, h))
            selected_zone.fill("white")

        screen.blit(selected_zone, (x, y))

        selected_zone.fill("white")
        selected_zone.blit(square, rect)
        pygame.draw.circle(square, TIFFANY, (50, 50), 49)
        square.blit(img, (35, 35))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen.fill(PURPLE)
                    square.fill(TIFFANY)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_select = True
                selected = [0, 0, 0, 0]
                selected[0] = event.pos[0]
                selected[1] = event.pos[1]
                selected[2] = event.pos[0]
                selected[3] = event.pos[1]
            elif event.type == pygame.MOUSEMOTION and mouse_select:
                selected[2] = event.pos[0]
                selected[3] = event.pos[1]
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_select = False
                selected[2] = event.pos[0]
                selected[3] = event.pos[1]

                selected_zone.fill("white")
                square = pygame.Surface((100, 100))
                square.fill(PURPLE)
                rect = square.get_rect()

        rect = rect.move(speed)

        if rect.left < 0 or rect.right > w:
            speed[0] = -speed[0]

        if rect.top < 0 or rect.bottom > h:
            speed[1] = -speed[1]

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
