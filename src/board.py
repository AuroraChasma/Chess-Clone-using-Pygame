import pygame as pg
import settings
pg.init()

class Board:
   
    def __init__(self):
        pass

    def draw(self, window):
        x = 0
        y = 0

        for part in settings.CHESS_BOARD:
            if part == 1:
                window.blit(settings.WHITE_PART, (x, y))

                x += 100
                if x == 800:
                    x = 0
                    y += 88

            elif part == 0:
                window.blit(settings.BLACK_PART, (x, y))
                x += 100
                if x == 800:
                    x = 0
                    y += 88

