#pragma once

#include "Tile.h"
import time

class Tile:
	
	""" The function creates the class variable of the tile
	Input- tile's x, tile's y, tile's value
	Output- none """
	def __init__(self, x, y, value):
		self._x = x
		self._y = y
		self._value = value
		self._possibleVals = []

	#the function returns the relative x and y of the tiles in the same box as the tile 
	def getAroundTiles(self):
		if self._x % 3 == 0:
			x_val_one = self._x + 1
			x_val_two = self._x + 2
		
		if self._x % 3 == 1:
			x_val_one = self._x + 1
			x_val_two = self._x - 1

		if self._x % 3 == 2:
			x_val_one = self._x - 1
			x_val_two = self._x - 2


		if self._y % 3 == 0:
			y_val_one = self._y + 1
			y_val_two = self._y + 2
		
		if self._y % 3 == 1:
			y_val_one = self._y + 1
			y_val_two = self._y - 1

		if self._y % 3 == 2:
			y_val_one = self._y - 1
			y_val_two = self._y - 2

		return ((x_val_one, x_val_two), (y_val_one, y_val_two))

	""" The function calculates the possible value of all the tiles that don't have a value
	Input- none
	Output- none """
	def calculatePossibleValues(self, board):
		if self._value == ".":
			self._possibleVals = list(range(1, 10))

			#removes the value of the tiles in the same row and line
			for i in range (0, 9):
				self.removeVal(board.getTile(self._x, i)._value)
				self.removeVal(board.getTile(i, self._y)._value)

			#removes the value of the tiles in the same box
			((x_val_one, x_val_two), (y_val_one, y_val_two)) = self.getAroundTiles()

			self.removeVal(board.getTile(self._x, y_val_one)._value)
			self.removeVal(board.getTile(self._x, y_val_two)._value)

			self.removeVal(board.getTile(x_val_one, self._y)._value)
			self.removeVal(board.getTile(x_val_two, self._y)._value)

			self.removeVal(board.getTile(x_val_one, y_val_one)._value)
			self.removeVal(board.getTile(x_val_two, y_val_two)._value)

			self.removeVal(board.getTile(x_val_one, y_val_two)._value)
			self.removeVal(board.getTile(x_val_two, y_val_one)._value)

	#checks if the values is in the possible values and removes it
	def removeVal(self, val):
		try:
			val = int(val)
		except:
			pass
		if val in self._possibleVals:
			self._possibleVals.remove(val)



	""" The function returns the piece on the tile
	Input- none
	Output- piec of the tile """
	def getValue(self):
		return self._value

	""" The function returns the piece on the tile
	Input- none
	Output- piec of the tile """
	def setValue(self, val):
		self._value = val

	""" The function sets inputed piece as tile piece
	Input- piece to set
	Output- none """
	def setPiece(self, value):
		self._value = value

	""" The function returns the x of the tile
	Input- none
	Output- the x of the tile """
	def getX(self):
		return self._x

	""" The function returns the x of the tile
	Input- none 
	Output- none """
	def getY(self):
		return self._y

	""" The function returns the x of the tile
	Input- none 
	Output- none """
	def getPossibleVals(self):
		return self._possibleVals