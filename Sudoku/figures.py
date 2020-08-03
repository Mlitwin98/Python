import pygame as p
from colors import *
from examples import *
from validator import validator

WIDTH = 900
HEIGHT = 900
screen = p.display.set_mode((WIDTH, HEIGHT))
screen.fill(white)
p.font.init()
font = p.font.SysFont('Arial', 40)
val = validator()


class square:
	def __init__(self, x=0, y=0, editable=None, value=0, color=black):
		self.x = x
		self.y = y
		self.rect = p.Rect(x, y, 100, 100)
		if value == 0:
			self.text_val = ''
		else:
			self.text_val = str(value)
		self.text = font.render(self.text_val, True, color)
		self.editable = editable
		self.focused = False
		self.value = value
		self.background = white

	def Draw(self):
		p.draw.rect(screen, self.background, self.rect, 0)
		p.draw.rect(screen, black, self.rect, 1)
		text_rect = self.text.get_rect(center=(self.x+50, self.y+50))
		screen.blit(self.text, text_rect)
		if self.focused:
			p.draw.rect(screen, green, self.rect, 5)

	def UpdateText(self, value):
		if self.editable:
			if value == 0:
				new_val = ''
			else:
				new_val = str(value)
			self.value = value
			self.text = font.render(new_val, True, lightblue)

	def CheckIfMouseOver(self):
		# noinspection PyArgumentList
		return self.rect.collidepoint(p.mouse.get_pos())

	def Click(self):
		for row in range(9):
			for sq in squares[row]:
				sq.focused = False
		self.focused = True

	def Erase(self):
		if self.editable:
			self.text = font.render('', True, white)
			self.value = 0

	def ChangeBackground(self, color):
		self.background = color

	def WrongAnswer(self):
		self.ChangeBackground(red)

	def PossibleAnswer(self):
		self.ChangeBackground(white)


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
			squares[i][j] = square(j * 100, i * 100, True, example[i][j])
		else:
			squares[i][j] = square(j * 100, i * 100, False, example[i][j])
# ----------------

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
# -----------------


# UPDATE SQUARES
def ChangeSquareText(text):
	for row in range(9):
		for col in range(9):
			if squares[row][col].focused:
				squares[row][col].UpdateText(text)
				check = val.CheckValue(squares, squares[row][col].value, row, col)
				if check[0] or check[1] or check[2]:
					squares[row][col].WrongAnswer()
				else:
					squares[row][col].PossibleAnswer()
				val.CheckWholeBoard(squares)


def EraseSquareText():
	for row in range(9):
		for sq in squares[row]:
			if sq.focused:
				sq.Erase()
				val.CheckWholeBoard(squares)
				sq.ChangeBackground(white)
# ---------------
