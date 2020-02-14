
import pygame
import os

class Visualizer:

    #inits pygame
    def __init__(self):
        pygame.init()
        self._size = (900, 900)
        self._screen = pygame.display.set_mode(self._size)
        pygame.display.set_caption('Sudoku')
        self._font = pygame.font.SysFont('Arial', 100)

    """Draws the board using pygame
    input- the current board 
    output- none
    """
    def drawBoard(self, pieceMsg):
        self._screen.fill( (255,255,255) )
        pygame.display.update()

        #draws the board in pygame
        i = 0
        while (i < 890):
            j = 0
            while (j < 890):
                """if i % 200:
                    if j % 200:
                        pygame.draw.rect(self._screen, (0 , 0 , 0), (i, j, 100, 100))
                    else:
                        pygame.draw.rect(self._screen, (255 , 255 , 255), (i, j, 100, 100))

                else:
                    if j % 200:
                        pygame.draw.rect(self._screen, (255 , 255 , 255), (i, j, 100, 100))
                    else:
                        pygame.draw.rect(self._screen, (0 , 0 , 0), (i, j, 100, 100))"""
                self._screen.blit(self._font.render(str(pieceMsg._tiles[int(i/ 100)][int(j/ 100)]._value), True, (100,100,100)), (i, j))
                pygame.display.update()
                j = j + 100

            i = i + 100
            pygame.display.update()

        #draws the baord in the console
        for i in range (0, 9):
            for j in range (0, 9):  
                #print(j)
                print(pieceMsg._tiles[int(i)][int(j)]._value, end =" ")
            print()
    

