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
            if part == 1: #1 --> white
                window.blit(settings.WHITE_PART, (x, y))

                x += settings.PART_WIDTH
                if x == settings.WINDOW_WIDTH:
                    x = 0
                    y += settings.PART_HEIGHT

            elif part == 0: #0--> black
                window.blit(settings.BLACK_PART, (x, y))
                x += settings.PART_WIDTH
                if x == settings.WINDOW_WIDTH:
                    x = 0
                    y += settings.PART_HEIGHT

