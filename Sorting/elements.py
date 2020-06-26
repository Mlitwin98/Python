import pygame as p
from colors import *


class Element:
	def __init__(self, width, height, x, y, color, value):
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.color = color
		self.value = value

	def Draw(self, screen):
		p.draw.rect(screen, self.color, p.Rect(self.x, self.y, self.width, self.height), 0)

	def SwitchPlaces(self, other, screen):
		screen.fill(lightgray)
		self.x, other.x = other.x, self.x

	def __lt__(self, other):
		return self.value < other.value

	def __gt__(self, other):
		return self.value > other.value
