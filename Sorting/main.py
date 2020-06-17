import colorsys as c
import pygame as p
import random as r
import buttons as b
import elements as e

from colors import *

p.init()
WIDTH = 900
HEIGHT = 900
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Sorting Algorithms')
font = p.font.SysFont('Arial', 25)
screen.fill(lightgray)


buttons = [b.Shuffler(120, 100, 'Shuffle', 5, 795),
		   b.BubbleSorter(120, 100, 'Bubble Sort', 130, 795),
		   b.SelectionSorter(130, 100, 'Selection Sort', 255, 795)]
elements = []
for i in range(b.numOfElements):
	color = c.hls_to_rgb(1 - i*10**-2, 0.5, 1)
	clr = [e * 255 for e in color]
	elements.append(e.Element(3, -i*2.5, 3*i, 790, clr, i))


def DrawButtons():
	for b in buttons:
		b.Draw(screen, font)


def DrawElements():
	for e in elements:
		e.Draw(screen)


def ShuffleStep():
	r1 = r.randint(0, b.numOfElements - 1)
	r2 = r.randint(0, b.numOfElements - 1)
	while r2 == r1:
		r2 = r.randint(0, b.numOfElements - 1)

	elements[r1], elements[r2] = elements[r2], elements[r1]
	elements[r1].SwitchPlaces(elements[r2], screen)


def ShuffleHandle():
	if b.shuffle and b.shuffleCount != 500:
		ShuffleStep()
		b.shuffleCount += 1
	if b.shuffleCount == 500:
		b.shuffleCount = 0
		b.shuffle = False


def BubbleSortHandle():
	if b.bubble and b.bubbleIndex[0] < len(elements):
		if b.bubbleIndex[1] < len(elements) - b.bubbleIndex[0] - 1:
			if elements[b.bubbleIndex[1]].value > elements[b.bubbleIndex[1] + 1].value:
				elements[b.bubbleIndex[1]], elements[b.bubbleIndex[1] + 1] = elements[b.bubbleIndex[1] + 1], elements[b.bubbleIndex[1]]
				elements[b.bubbleIndex[1]].SwitchPlaces(elements[b.bubbleIndex[1] + 1], screen)
			b.bubbleIndex[1] += 1
		else:
			b.bubbleIndex[0] += 1
			b.bubbleIndex[1] = 0
	elif b.bubbleIndex[0] == len(elements):
		b.bubble = False


running = True
while running:
	p.display.update()

	BubbleSortHandle()
	ShuffleHandle()
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
