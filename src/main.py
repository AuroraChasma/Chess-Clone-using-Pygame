import pygame as pg
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, chess_board, WHITE_PART, BLACK_PART
from board import Board
pg.init()

class ChessGame:
    board = Board()
    
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

        #setting up window
        self.window = pg.display.set_mode((self.window_width, self.window_height))
        pg.display.set_caption("Chess Clone")

    def run(self):
        #main game loop
        runGame = True
        while runGame:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    runGame = False
        x = 0
        y = 0

        for part in chess_board:
            if part == 1:
                self.window.blit(WHITE_PART, (x, y))

                x += 100
                if x == 800:
                    x = 0
                    y += 88

            elif part == 0:
                self.window.blit(BLACK_PART, (x, y))
                x += 100
                if x == 800:
                    x = 0
                    y += 88

            pg.display.update()
                


if __name__ == "__main__":
    chess_game = ChessGame(WINDOW_WIDTH, WINDOW_HEIGHT)
    chess_game.run()

