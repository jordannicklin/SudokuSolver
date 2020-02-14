
BOARD_SIZE = 9

import Tile

class Board():
	""" The function creates the class variable of the board
	Input- none
	Output- none """
	def __init__(self, boardVal):
		self._tiles = []                                                           
		for y in range (0, BOARD_SIZE):             
			new = []                 
			for x in range (0, BOARD_SIZE):   
				new.append(Tile.Tile(x,y, boardVal[y][x])) 
			self._tiles.append(new)
		self.calculateTilesPossibleValues()

	""" The function calculates the possible value of all the tiles that don't have a value
	Input- none
	Output- none """
	def calculateTilesPossibleValues(self):
		for y in range (0, BOARD_SIZE):
			for x in range (0, BOARD_SIZE):  
				self._tiles[int(y)][int(x)].calculatePossibleValues(self)

	def updatePossibleValues(self, tileY, tileX ,val):
		for y in range (0, BOARD_SIZE):
			for x in range (0, BOARD_SIZE): 
				self._tiles[int(tileY)][int(x)].removeVal(val)
				self._tiles[int(y)][int(tileX)].removeVal(val)
		((x_val_one, x_val_two), (y_val_one, y_val_two)) = self._tiles[int(tileY)][int(tileX)].getAroundTiles()
	
		self.getTile(x_val_one, y_val_one).removeVal(val)
		self.getTile(x_val_one, y_val_two).removeVal(val)

		self.getTile(x_val_two, y_val_one).removeVal(val)
		self.getTile(x_val_two, y_val_two).removeVal(val)
		
		self.getTile(tileX, y_val_one).removeVal(val)
		self.getTile(tileX, y_val_two).removeVal(val)

		self.getTile(x_val_two, tileY).removeVal(val)
		self.getTile(x_val_two, tileY).removeVal(val)


	""" The function returns a tile in the place of inputed x,y
	Input- x,y of the tile to get 
	Output- tile in the place of x,y"""
	def getTile(self, x, y):
		#returns tile in x and y
		return self._tiles[int(y)][int(x)]