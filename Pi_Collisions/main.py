import os
import pygame
from pygame import mixer

import COLOURS

WIDTH, HEIGHT = 1800, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pi Collisions")
FPS = 60
TIME_STEP = 10

k = 2
n = 1
SMALL_SQUARE_WIDTH, SMALL_SQUARE_HEIGHT = 50, 50
BIG_SQUARE_WIDTH, BIG_SQUARE_HEIGHT = SMALL_SQUARE_WIDTH * k, SMALL_SQUARE_HEIGHT * k

mixer.init()
mixer.music.set_volume(0.2)
CLACK = pygame.mixer.Sound(os.path.join("Assets", 'clack.wav'))

pygame.font.init()
my_font = pygame.font.SysFont('arial', 30)


def velocity1(u_0, m_1, m_2, u_2):
    m = m_1 + m_2
    u_1 = (((2 * m_2) / m) * u_2) + (((m_1 - m_2) / m) * u_0)

    return u_1


def draw_window(square_1, square_2, text_surface):
    WIN.fill(COLOURS.LAVENDER_BLUSH)
    WIN.blit(text_surface, (1500, 0))
    pygame.draw.line(WIN, COLOURS.BLACK, (5, 0), (5, 600), 3)
    pygame.draw.line(WIN, COLOURS.BLACK, (5, 600), (1800, 600), 3)
    pygame.draw.rect(WIN, COLOURS.RUSSIAN_GREEN, square_1, 4)
    pygame.draw.rect(WIN, COLOURS.BLACK, square_2, 4)
    pygame.display.update()


def main():
    square_1 = pygame.Rect(100, 600 - SMALL_SQUARE_HEIGHT, SMALL_SQUARE_WIDTH, SMALL_SQUARE_HEIGHT)
    u_1 = 0
    m_1 = 1

    square_2 = pygame.Rect(700, 600 - BIG_SQUARE_HEIGHT, BIG_SQUARE_WIDTH, BIG_SQUARE_HEIGHT)
    u_2 = -9
    m_2 = 100

    collisions = 0

    clock = pygame.time.Clock()
    run = True

    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        square_1.x += u_1
        square_2.x += u_2
        text_surface = my_font.render(f"Collisions:{str(collisions)}", False, COLOURS.BLACK)

        if pygame.Rect.colliderect(square_1, square_2):

            pygame.mixer.Sound.play(CLACK)

            collisions += 1

            u_0_1 = u_1
            u_0_2 = u_2

            u_1 = velocity1(u_0_1, m_1, m_2, u_0_2)
            u_2 = velocity1(u_0_2, m_2, m_1, u_0_1)

            print(f"x1:{square_1.x} x2:{square_2.x}")
            print(f"u1={u_1} u2={u_2}")
            print(f"collions:{collisions}")

        elif square_1.x < 5:

            pygame.mixer.Sound.play(CLACK)
            collisions += 1
            u_1 *= -1

            print(f"x1:{square_1.x} x2:{square_2.x}")
            print(f"u1={u_1} u2={u_2}")
            print(f"collions:{collisions}")

        draw_window(square_1, square_2, text_surface)
    print(f"collions:{collisions}")
    pygame.quit()


if __name__ == '__main__':
    main()
