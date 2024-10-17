import pygame as pg

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700

WHITE_PART = pg.image.load("../assets/board/white_board_part")
BLACK_PART = pg.image.load("../assets/board/black_board_part")


#1 --> white, 0 --> black
board = [1, 0, 1, 0, 1, 0, 1, 0,
         0, 1, 0, 1, 0, 1, 0, 1,
         1, 0, 1, 0, 1, 0, 1, 0,
         0, 1, 0, 1, 0, 1, 0, 1,
         1, 0, 1, 0, 1, 0, 1, 0,
         0, 1, 0, 1, 0, 1, 0, 1,
         1, 0, 1, 0, 1, 0, 1, 0,
         0, 1, 0, 1, 0, 1, 0, 1,]