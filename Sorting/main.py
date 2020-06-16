import pygame as p
import colorsys as c
import random as r

lightgray = (211, 211, 211)
white = (255, 255, 255)
black = (0, 0, 0)

p.init()
WIDTH = 900
HEIGHT = 900
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Sorting Algorithms')
font = p.font.SysFont('Arial', 25)
screen.fill(lightgray)


class Element:
	def __init__(self, width, height, x, y, color, value):
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.color = color
		self.value = value

	def Draw(self):
		p.draw.rect(screen, self.color, p.Rect(self.x, self.y, self.width, self.height), 0)

	def SwitchPlaces(self, other):
		screen.fill(lightgray)
		self.x, other.x = other.x, self.x


class MyButton:
	def __init__(self, width, height, text, x, y):
		self.width = width
		self.height = height
		self.text = text
		self.x = x
		self.y = y
		self.rect = p.Rect(x, y, width, height)

	def Draw(self):
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
		for i in range(1000):
			r1 = r.randint(0, 99)
			r2 = r.randint(0, 99)
			while r2 == r1:
				r2 = r.randint(0, 99)

			elements[r1], elements[r2] = elements[r2], elements[r1]
			elements[r1].SwitchPlaces(elements[r2])


class BubbleSorter(MyButton):
	def Click(self):
		print('s')


elements = []
buttons = [Shuffler(120, 100, 'Shuffle', 5, 795), BubbleSorter(120, 100, 'Bubble Sort', 130, 795)]
for i in range(100):
	color = c.hls_to_rgb(1 - i*10**-2, 0.5, 1)
	clr = [e * 255 for e in color]
	elements.append(Element(9, -i*2.5, 9*i, 790, clr, i))

def DrawButtons():
	for b in buttons:
		b.Draw()


def DrawElements():
	for e in elements:
		e.Draw()


running = True
while running:
	p.display.update()

	DrawButtons()
	DrawElements()

	for event in p.event.get():
		if event.type == p.QUIT:
			running = False
			p.quit()
			quit()
		if event.type == p.MOUSEBUTTONDOWN:
			for button in buttons:
				if button.CheckIfMouseOver():
					button.Click()
