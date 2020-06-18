import pygame as p
from colors import *


class MyButton:
	def __init__(self, width, height, text, x, y):
		self.width = width
		self.height = height
		self.text = text
		self.x = x
		self.y = y
		self.rect = p.Rect(x, y, width, height)

	def Draw(self, screen, font):
		p.draw.rect(screen, white, self.rect, 0)
		p.draw.rect(screen, black, self.rect, 2)

		x = self.x + self.width/2
		y = self.y + self.height/2
		text = font.render(self.text, True, black)
		text_rect = text.get_rect(center=(x, y))
		screen.blit(text, text_rect)

	def CheckIfMouseOver(self):
		# noinspection PyArgumentList
		return self.rect.collidepoint(p.mouse.get_pos())


class Shuffler(MyButton):
	def __init__(self, width, height, text, x, y):
		MyButton.__init__(self, width, height, text, x, y)
		self.shuffle = False

	def Click(self):
		self.shuffle = True


class BubbleSorter(MyButton):
	def __init__(self, width, height, text, x, y):
		MyButton.__init__(self, width, height, text, x, y)
		self.bubbleIndex = [0, 0]
		self.sort = False

	def Click(self):
		self.bubbleIndex = [0, 0]
		self.sort = True


class SelectionSorter(MyButton):
	def __init__(self, width, height, text, x, y):
		MyButton.__init__(self, width, height, text, x, y)
		self.selectionIndex = [0, 0]
		self.sort = False

	def Click(self):
		self.selectionIndex = [0, 0]
		self.sort = True


class ShellSorter(MyButton):
	def __init__(self, width, height, text, x, y, gap):
		MyButton.__init__(self, width, height, text, x, y)
		self.gap = gap
		self.tmp = gap
		self.sort = False

	def Click(self):
		self.gap = self.tmp
		# ZROBIC COS Z SHUFFLEM
		#self.shuffle = False
		self.sort = True


class CocktailSorter(MyButton):
	def __init__(self, width, height, text, x, y, start, end):
		MyButton.__init__(self, width, height, text, x, y)
		self.tmp = (start, end)
		self.cocktailStart = start
		self.cocktailEnd = end
		self.sort = False

	def Click(self):
		self.cocktailStart = self.tmp[0]
		self.cocktailEnd = self.tmp[1]
		self.sort = True


class MergeSorter(MyButton):
	def __init__(self, width, height, text, x, y):
		MyButton.__init__(self, width, height, text, x, y)
		self.sort = False

	def Click(self):
		self.sort = True
