import pygame as p
from colors import *

WIDTH = 900
HEIGHT = 1000
screen = p.display.set_mode((WIDTH, HEIGHT))
screen.fill(white)
p.font.init()
font = p.font.SysFont('Arial', 40)

example = [[6, 3, 0, 0, 2, 0, 0, 0, 9],
		   [0, 4, 0, 5, 3, 1, 0, 0, 2],
		   [0, 7, 5, 0, 4, 9, 0, 3, 1],
		   [8, 0, 0, 4, 0, 6, 1, 0, 0],
		   [0, 0, 0, 2, 1, 0, 3, 9, 6],
		   [0, 0, 0, 7, 0, 3, 2, 0, 4],
		   [3, 8, 7, 0, 0, 0, 4, 0, 0],
		   [4, 0, 2, 1, 0, 0, 0, 6, 3],
		   [0, 0, 0, 0, 7, 0, 0, 0, 0]]


class square:
	def __init__(self, x=0, y=0, scr=None, editable=None, text=0, color=black):
		self.x = x
		self.y = y
		self.rect = p.Rect(x, y, 100, 100)
		if text == 0:
			self.text_val = ''
		else:
			self.text_val = str(text)
		self.text = font.render(self.text_val, True, color)
		self.screen = scr
		self.editable = editable
		self.focused = False
		self.value = text

	def Draw(self):
		p.draw.rect(self.screen, black, self.rect, 1)
		text_rect = self.text.get_rect(center=(self.x+50, self.y+50))
		self.screen.blit(self.text, text_rect)

	def UpdateText(self, text):
		if self.editable:
			if text == 0:
				new_val = ''
			else:
				new_val = str(text)
			self.value = text
			p.draw.rect(self.screen, white, self.rect, 0)
			self.text = font.render(new_val, True, lightblue)
			p.draw.rect(self.screen, green, self.rect, 5)

	def CheckIfMouseOver(self):
		# noinspection PyArgumentList
		return self.rect.collidepoint(p.mouse.get_pos())

	def Click(self):
		for row in range(9):
			for sq in squares[row]:
				p.draw.rect(self.screen, white, sq.rect, 5)
				sq.focused = False
		p.draw.rect(self.screen, green, self.rect, 5)
		self.focused = True

	def Erase(self):
		if self.editable:
			self.text = font.render('', True, white)
			self.value = 0
			p.draw.rect(self.screen, white, self.rect, 0)
			p.draw.rect(self.screen, green, self.rect, 5)

	def ChangeBackground(self, color):
		if self.editable and self.focused:
			p.draw.rect(self.screen, color, self.rect, 0)
			p.draw.rect(self.screen, green, self.rect, 5)
		else:
			p.draw.rect(self.screen, color, self.rect, 0)
			p.draw.rect(self.screen, white, self.rect, 5)


class line:
	def __init__(self, x, y, horizontal):
		self.x = x
		self.y = y
		if horizontal:
			self.width = 900
			self.height = 4
		else:
			self.width = 4
			self.height = 900
		self.rect = p.Rect(x, y, self.width, self.height)

	def Draw(self):
		p.draw.rect(screen, black, self.rect)


# INITIALIZE SQUARES
squares = [[square() for i in range(9)] for j in range(9)]
for i in range(9):
	for j in range(9):
		if example[i][j] == 0:
			squares[i][j] = square(j * 100, i * 100, screen, True, example[i][j])
		else:
			squares[i][j] = square(j * 100, i * 100, screen, False, example[i][j])

# INITIALIZE LINES
lines = []
for i in range(2):
	for j in range(1, 3):
		if i == 0:
			lines.append(line(j*300, i, False))
		else:
			lines.append(line(i-1, j*300, True))


def DrawSquares():
	for row in range(9):
		for sq in squares[row]:
			sq.Draw()


def DrawLines():
	for ln in lines:
		ln.Draw()


def ChangeSquareText(text):
	for row in range(9):
		for col in range(9):
			if squares[row][col].focused:
				mistake = False
				squares[row][col].UpdateText(text)
				check = CheckValue(squares[row][col].value, row, col)
				if check[0] or check[1] or check[2]:
					mistake = True
				if mistake:
					WrongAnswer(row, col)
				else:
					PossibleAnswer(row, col)


def CheckWholeBoard():
	for row in range(9):
		for col in range(9):
			if squares[row][col].editable and not squares[row][col].focused:
				mistake = False
				check = CheckValue(squares[row][col].value, row, col)
				if check[0] or check[1] or check[2]:
					mistake = True
				if mistake:
					WrongAnswer(row, col)
				else:
					PossibleAnswer(row, col)


def EraseSquareText():
	for row in range(9):
		for sq in squares[row]:
			if sq.focused:
				sq.Erase()


# CHECK ANSWER
def CheckIfValueInBigSquare(value, squareRow, squareCol):
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


def CheckIfValueInRow(value, row):
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


def CheckIfValueInColumn(value, col):
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


def CheckValue(value, row, column):
	r = CheckIfValueInRow(value, row)
	c = CheckIfValueInColumn(value, column)
	s = CheckIfValueInBigSquare(value, row//3, column//3)
	return r, c, s


def WrongAnswer(row, col):
	squares[row][col].ChangeBackground(red)


def PossibleAnswer(row, col):
	squares[row][col].ChangeBackground(white)
