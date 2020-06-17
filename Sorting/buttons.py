import pygame as p
from colors import *

numOfElements = 300
shuffle = False
bubble = False
selection = False
shuffleCount = 0
bubbleIndex = [0, 0]
selectionIndex = [0, 0]


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
	def Click(self):
		global shuffle, bubble, shuffleCount
		shuffleCount = 0
		bubble = False
		shuffle = True


class BubbleSorter(MyButton):
	def Click(self):
		global bubble, bubbleIndex
		bubbleIndex = [0, 0]
		bubble = True


class SelectionSorter(MyButton):
	def Click(self):
		global selection, selectionIndex
		selectionIndex = [0, 0]
		selection = True