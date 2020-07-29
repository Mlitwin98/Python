class validator:
	def __init__(self):
		pass

	@staticmethod
	def CheckIfEmptySpaces(squares):
		for row in range(9):
			for sq in squares[row]:
				if sq.value == 0:
					return True
		return False

	# 3x3 SQUARE
	@staticmethod
	def CheckIfValueInBigSquare(squares, value, squareRow, squareCol):
		if value == 0:
			return False
		count = 0
		for row in range(3):
			for col in range(3):
				if value == squares[row + 3 * squareRow][col + 3 * squareCol].value:
					count += 1
		if count > 1:
			return True
		else:
			return False

	# ROW
	@staticmethod
	def CheckIfValueInRow(squares, value, row):
		if value == 0:
			return False
		count = 0
		for sq in squares[row]:
			if sq.value == value:
				count += 1
		if count > 1:
			return True
		else:
			return False

	# COLUMN
	@staticmethod
	def CheckIfValueInColumn(squares, value, col):
		if value == 0:
			return False
		count = 0
		for r in range(9):
			if squares[r][col].value == value:
				count += 1
		if count > 1:
			return True
		else:
			return False

	# 3x3, ROW, COLUMN
	def CheckValue(self, squares, value, row, column):
		r = self.CheckIfValueInRow(squares, value, row)
		c = self.CheckIfValueInColumn(squares, value, column)
		s = self.CheckIfValueInBigSquare(squares, value, row // 3, column // 3)
		return r, c, s

	def CheckWholeBoard(self, squares):
		result = True
		for row in range(9):
			for col in range(9):
				if squares[row][col].editable:
					check = self.CheckValue(squares, squares[row][col].value, row, col)
					if check[0] or check[1] or check[2]:
						squares[row][col].WrongAnswer()
						result = False
					else:
						squares[row][col].PossibleAnswer()
		return result
