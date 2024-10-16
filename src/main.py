import pygame as pg
import settings
pg.init()

class ChessGame:
    
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

                


if __name__ == "__main__":
    chess_game = ChessGame(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
    chess_game.run()

