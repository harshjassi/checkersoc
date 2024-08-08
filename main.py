# main.py
import pygame
from gui.constants import WIDTH, HEIGHT
from gui.game import Game

def main():
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Checkers AI')

    game = Game(WIN)
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // 100
    col = x // 100
    return row, col

if __name__ == "__main__":
    main()
