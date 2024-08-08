# checkers/board.py
import pygame
from .piece import Piece
from gui.constants import SQUARE_SIZE, RED, WHITE, BLACK

class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw(self, win):
        self.draw_squares(win)
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(8):
            for col in range(row % 2, 8, 2):
                pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(8):
            self.board.append([])
            for col in range(8):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, 'white'))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, 'red'))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = 0, piece
        piece.move(row, col)

        if row == 0 or row == 7:
            piece.make_king()
            if piece.color == 'red':
                self.red_kings += 1
            else:
                self.white_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == 'red':
                    self.red_left -= 1
                else:
                    self.white_left -= 1

    def winner(self):
        if self.red_left <= 0:
            return 'white'
        elif self.white_left <= 0:
            return 'red'
        return None
