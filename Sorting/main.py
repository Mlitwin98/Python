import colorsys as c
import pygame as p
import random as r
import buttons as b
import elements as e

from colors import *

p.init()
numOfElements = 300
WIDTH = 900
HEIGHT = 900
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Sorting Algorithms')
font = p.font.SysFont('Arial', 25)
screen.fill(lightgray)


buttons = [b.Shuffler(120, 100, 'Shuffle', 5, 795),
		   b.BubbleSorter(120, 100, 'Bubble Sort', 130, 795),
		   b.SelectionSorter(130, 100, 'Selection Sort', 255, 795),
		   b.ShellSorter(120, 100, 'Shell Sort', 390, 795)]
elements = []
for i in range(numOfElements):
	color = c.hls_to_rgb(1 - i*10**-2, 0.5, 1)
	clr = [e * 255 for e in color]
	elements.append(e.Element(WIDTH/numOfElements, -i*2.5, WIDTH/numOfElements*i, 790, clr, i))


def DrawButtons():
	for b in buttons:
		b.Draw(screen, font)


def DrawElements():
	for e in elements:
		e.Draw(screen)


def ShuffleStep():
	r1 = r.randint(0, numOfElements - 1)
	r2 = r.randint(0, numOfElements - 1)
	while r2 == r1:
		r2 = r.randint(0, numOfElements - 1)

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

# To fix
def SelectionSortHandle():
	if b.selection and b.selectionIndex[0] < len(elements) - 1:
		min_i = b.selectionIndex[0]
		b.selectionIndex[1] = min_i + 1
		while b.selectionIndex[1] < len(elements):
			if elements[b.selectionIndex[1]].value < elements[min_i].value:
				min_i = b.selectionIndex[1]

			b.selectionIndex[1] += 1
		else:
			elements[min_i], elements[b.selectionIndex[0]] = elements[b.selectionIndex[0]], elements[min_i]
			elements[b.selectionIndex[0]].SwitchPlaces(elements[min_i], screen)
			b.selectionIndex[0] += 1
	elif b.selectionIndex[0] == len(elements):
		b.bubble = False

ind = b.gap
def ShellSortHandle():
	global ind
	if b.shell and b.gap > 0:
		if ind < len(elements):
			tmp = elements[ind]
			j = ind
			while j >= b.gap and elements[j-b.gap].value > tmp.value:
				elements[j], elements[j-b.gap] = elements[j-b.gap], elements[j]
				elements[j].SwitchPlaces(elements[j-b.gap], screen)
				j -= b.gap
			elements[j] = tmp
			ind += 1
		else:
			b.gap //= 2
			ind = b.gap
	elif b.gap == 0:
		b.shell = False


running = True
while running:
	p.display.update()

	ShuffleHandle()
	BubbleSortHandle()
	SelectionSortHandle()
	ShellSortHandle()
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
