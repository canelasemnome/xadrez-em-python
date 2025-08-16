import pygame as p
import ChessEngine

p.init()
WIDTH = HEIGHT = 512 #400 is another option
DIMENSION = 8 #dimensions of a chess board are 8x8                                                                               \\ x
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #for animations later on
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called exactly once in the main
'''

def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
    IMAGES['wp'] = p.transform.scale(p.images.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
#Note: we can access an image by saying 'IMAGES['wp']'

'''
The main driver for our code. This will handle user input and updating the graphics
'''

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages() #only do this once, before the while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        drawGameState(screen, gs):
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Responsible for all the gra
'''
def drawGameState(screen, gs)
    drawBoard(screen) #draw squares on the board
    drawPieces(screen, gs.board) #

if __name__ == " main ":
    main()