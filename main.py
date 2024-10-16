import pygame as pg
from general_settings import *



class ChessGame:
    window = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Chess Clone")

    def __init__(self):
        pass

    def run(self):
        runGame = True
        while runGame:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    runGame = False

                


if __name__ == "__main__":
    chess_game = ChessGame()
    chess_game.run()

