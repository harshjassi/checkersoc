# gui/game.py
import pygame
from .constants import RED, WHITE, SQUARE_SIZE, WIDTH, HEIGHT
from checkers.board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = 'red'

    def select(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0:
            self.board.move(self.selected, row, col)
            return True

        return False

    def reset(self):
        self._init()
