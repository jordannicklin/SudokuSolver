
BOARD_SIZE = 9

from enum import Enum

import Board
import time

class SudokuSolver:

	""" The function creates the dynamic variabels
	Input- none
	Output- none """
	def __init__(self):
		pass

	""" The function looks for a tile with only one possible value and assigns that value as the tile value
	Input- board
	Output- if the sudoku is solved """
	def next(self, board):
		for i in range (0, BOARD_SIZE):
			for j in range (0, BOARD_SIZE):  
				#print((board._tiles[int(i)][int(j)]._possibleVals))
				if len(board._tiles[int(i)][int(j)]._possibleVals) == 1:
					board._tiles[int(i)][int(j)].setValue(board._tiles[int(i)][int(j)]._possibleVals[0])
					board._tiles[int(i)][int(j)]._possibleVals = []
					board.updatePossibleValues(int(i),int(j) , board._tiles[int(i)][int(j)]._value)
					return False
		return True