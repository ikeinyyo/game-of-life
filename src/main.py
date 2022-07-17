import argparse
import time

import numpy as np
import pygame

COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170,  170)
COLOR_ALIVE_NEXT = (255, 255, 255)
SIZE = 15
WIDTH = 60
HEIGHT = 80
MIN_SPEED = 1
MAX_SPEED = 20

# pylint: disable=no-member


def init_game(initialize_random=False):
    pygame.init()
    pygame.display.set_caption("Game of Life - Python")
    screen = pygame.display.set_mode((HEIGHT * SIZE, WIDTH * SIZE))
    cells = np.random.randint(
        0, 2, (WIDTH, HEIGHT)) if initialize_random else np.zeros((WIDTH, HEIGHT))
    screen.fill(COLOR_GRID)
    pygame.display.flip()
    update_and_draw(screen, cells)
    return screen, cells


def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, column in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, column-1:column+2]
                       ) - cells[row, column]
        color = COLOR_BG if cells[row, column] == 0 else COLOR_ALIVE_NEXT

        if cells[row, column] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                updated_cells[row, column] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        else:
            if alive == 3:
                updated_cells[row, column] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        pygame.draw.rect(screen, color, (column * size,
                         row * size, size - 1, size - 1))
    return updated_cells


def update_and_draw(screen, cells, running=False):
    cells = update(screen, cells, SIZE, running)
    pygame.display.update()
    return cells


def edit_grid(screen, cells, mouse_pressed):
    if mouse_pressed[0] or mouse_pressed[2]:
        pos = pygame.mouse.get_pos()
        cells[pos[1] // SIZE, pos[0] // SIZE] = mouse_pressed[0]
        update_and_draw(screen, cells)


def manage_speed(event, speed):
    if event.key == pygame.K_UP:
        return min(speed+1, MAX_SPEED)
    if event.key == pygame.K_DOWN:
        return max(speed - 1, MIN_SPEED)
    return speed


def manage_pause(event, running):
    if event.key == pygame.K_SPACE:
        return not running
    return running


def main(initialize_random=False):
    screen, cells = init_game(initialize_random)
    running = False
    speed = MAX_SPEED / 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = manage_pause(event, running)
                speed = manage_speed(event, speed)
                update_and_draw(screen, cells)
            edit_grid(screen, cells, pygame.mouse.get_pressed())

        if running:
            screen.fill(COLOR_GRID)
            cells = update_and_draw(screen, cells, True)
            time.sleep(1/speed)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--random', required=False, action="store_true")
    args = parser.parse_args()
    main(args.random)
