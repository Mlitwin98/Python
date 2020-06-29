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
	def __init__(self, x, y, scr, editable, text=0, color=black):
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
			p.draw.rect(self.screen, white, self.rect, 0)
			self.text = font.render(new_val, True, lightblue)
			p.draw.rect(self.screen, green, self.rect, 5)
			self.value = text

	def CheckIfMouseOver(self):
		# noinspection PyArgumentList
		return self.rect.collidepoint(p.mouse.get_pos())

	def Click(self):
		for sq in sqaures:
			p.draw.rect(self.screen, white, sq.rect, 5)
			sq.focused = False
		p.draw.rect(self.screen, green, self.rect, 5)
		self.focused = True


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
sqaures = []
for i in range(9):
	for j in range(9):
		if example[i][j] == 0:
			sqaures.append(square(j*100, i*100, screen, True, example[i][j]))
		else:
			sqaures.append(square(j * 100, i * 100, screen, False, example[i][j]))

# INITIALIZE LINES
lines = []
for i in range(2):
	for j in range(1, 3):
		if i == 0:
			lines.append(line(j*300, i, False))
		else:
			lines.append(line(i-1, j*300, True))


def DrawSquares():
	for sq in sqaures:
		sq.Draw()


def DrawLines():
	for ln in lines:
		ln.Draw()


def ChangeSquareText(text):
	for sq in sqaures:
		if sq.focused:
			sq.UpdateText(text)
