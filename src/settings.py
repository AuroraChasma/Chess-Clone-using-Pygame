import pygame as pg


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700

PART_WIDTH = WINDOW_WIDTH//8
PART_HEIGHT = WINDOW_HEIGHT//8
WHITE_PART = pg.transform.scale(pg.image.load("../assets/board/white_board_part"), (PART_WIDTH, PART_HEIGHT))
BLACK_PART = pg.transform.scale(pg.image.load("../assets/board/black_board_part"), (PART_WIDTH, PART_HEIGHT))


#1 --> white, 0 --> black
CHESS_BOARD = [ 1, 0, 1, 0, 1, 0, 1, 0,
                0, 1, 0, 1, 0, 1, 0, 1,
                1, 0, 1, 0, 1, 0, 1, 0,
                0, 1, 0, 1, 0, 1, 0, 1,
                1, 0, 1, 0, 1, 0, 1, 0,
                0, 1, 0, 1, 0, 1, 0, 1,
                1, 0, 1, 0, 1, 0, 1, 0,
                0, 1, 0, 1, 0, 1, 0, 1]