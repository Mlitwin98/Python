import colorsys as c
import random as r
import elements as e

from buttons import *
from colors import *

# PYGAME
p.init()
WIDTH = 900
HEIGHT = 900
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Sorting Algorithms')
font = p.font.SysFont('Arial', 25)
screen.fill(lightgray)

# FILL ELEMENTS
numOfElements = 300
shuffleCount = 0
elements = []
for i in range(numOfElements):
	color = c.hls_to_rgb(1 - i * 10 ** -2, 0.5, 1)
	clr = [e * 255 for e in color]
	elements.append(e.Element(WIDTH / numOfElements, -i * 2, WIDTH / numOfElements * i, 790, clr, i))

# FILL BUTTONS
sh = Shuffler(120, 100, 'Shuffle', 5, 795)
bs = BubbleSorter(120, 100, 'Bubble Sort', 130, 795)
ss = SelectionSorter(130, 100, 'Selection Sort', 255, 795)
shs = ShellSorter(110, 100, 'Shell Sort', 390, 795, numOfElements//2)
cs = CocktailSorter(120, 100, 'Cocktail Sort', 505, 795, 0, numOfElements-1)
ins = InsertionSorter(130, 100, 'Insertion Sort', 630, 795)
ps = PancakeSorter(130, 100, 'Pancake Sort', 765, 795, len(elements))
buttons = [sh, bs, ss, shs, cs, ins, ps]


# DRAWING
def DrawButtons():
	for bt in buttons:
		bt.Draw(screen, font)


def DrawElements():
	for e in elements:
		e.Draw(screen)


# SHUFFLE
def ShuffleStep():
	r1 = r.randint(0, shuffleCount)

	elements[r1], elements[shuffleCount] = elements[shuffleCount], elements[r1]
	elements[r1].SwitchPlaces(elements[shuffleCount], screen)


def ShuffleHandle():
	global shuffleCount
	if sh.shuffle and shuffleCount != numOfElements:
		ShuffleStep()
		shuffleCount += 1
	if shuffleCount == numOfElements:
		shuffleCount = 0
		sh.shuffle = False


# SORTING
	# BUBBLE
def BubbleSort():
	if bs.sort and bs.bubbleIndex[0] < len(elements) and not sh.shuffle:
		while bs.bubbleIndex[1] < len(elements) - bs.bubbleIndex[0] - 1:
			if elements[bs.bubbleIndex[1]] > elements[bs.bubbleIndex[1] + 1]:
				elements[bs.bubbleIndex[1]], elements[bs.bubbleIndex[1] + 1] = elements[bs.bubbleIndex[1] + 1], elements[
					bs.bubbleIndex[1]]
				elements[bs.bubbleIndex[1]].SwitchPlaces(elements[bs.bubbleIndex[1] + 1], screen)
			bs.bubbleIndex[1] += 1
		else:
			bs.bubbleIndex[0] += 1
			bs.bubbleIndex[1] = 0
	elif sh.shuffle:
		bs.sort = False


	# SELECTION
def SelectionSort():
	if ss.sort and ss.selectionIndex[0] < len(elements) - 1 and not sh.shuffle:
		min_i = ss.selectionIndex[0]
		ss.selectionIndex[1] = min_i + 1
		while ss.selectionIndex[1] < len(elements):
			if elements[ss.selectionIndex[1]] < elements[min_i]:
				min_i = ss.selectionIndex[1]

			ss.selectionIndex[1] += 1
		else:
			elements[min_i], elements[ss.selectionIndex[0]] = elements[ss.selectionIndex[0]], elements[min_i]
			elements[ss.selectionIndex[0]].SwitchPlaces(elements[min_i], screen)
			ss.selectionIndex[0] += 1
	elif sh.shuffle:
		ss.sort = False


	# SHELL
ind = shs.gap


def ShellSort():
	global ind
	if shs.sort and shs.gap > 0 and not sh.shuffle:
		if ind < len(elements):
			tmp = elements[ind]
			j = ind
			while j >= shs.gap and elements[j - shs.gap] > tmp:
				elements[j], elements[j - shs.gap] = elements[j - shs.gap], elements[j]
				elements[j].SwitchPlaces(elements[j - shs.gap], screen)
				j -= shs.gap
			elements[j] = tmp
			ind += 1
		else:
			shs.gap //= 2
			ind = shs.gap
	elif sh.shuffle:
		shs.sort = False


	# COCKTAIL
def CocktailSort():
	if cs.sort and not sh.shuffle:
		cs.sort = False

		for i in range(cs.cocktailStart, cs.cocktailEnd):
			if elements[i] > elements[i + 1]:
				elements[i], elements[i + 1] = elements[i + 1], elements[i]
				elements[i].SwitchPlaces(elements[i + 1], screen)
				cs.sort = True

		cs.sort = False
		cs.cocktailEnd -= 1

		for i in range(cs.cocktailEnd - 1, cs.cocktailStart - 1, -1):
			if elements[i] > elements[i + 1]:
				elements[i], elements[i + 1] = elements[i + 1], elements[i]
				elements[i].SwitchPlaces(elements[i + 1], screen)
				cs.sort = True

		cs.cocktailStart += 1
	elif sh.shuffle:
		cs.sort = False


	# INSERTION
def InsertionSort():
	if ins.sort and not sh.shuffle:
		if ins.index < len(elements):
			tmp = elements[ins.index]
			j = ins.index - 1
			while j >= 0 and tmp < elements[j]:
				elements[j+1], elements[j] = elements[j], elements[j+1]
				elements[j+1].SwitchPlaces(elements[j], screen)
				j -= 1

			elements[j+1] = tmp
			tmp.SwitchPlaces(elements[j+1], screen)
			ins.index += 1
		elif ins.index == len(elements):
			ins.sort = False


	# PANCAKE
def flip(i):
	start = 0
	while start < i:
		elements[start], elements[i] = elements[i], elements[start]
		elements[start].SwitchPlaces(elements[i], screen)
		start += 1
		i -= 1


def PancakeSort():
	if ps.sort and not sh.shuffle:
		if ps.size > 1:
			maxI = 0
			for i in range(0, ps.size):
				if elements[i] > elements[maxI]:
					maxI = i

			if maxI != ps.size-1:
				flip(maxI)
				flip(ps.size-1)
			ps.size -= 1
	elif ps.size == 1:
		ps.sort = False


# GAME LOOP
running = True
while running:
	p.display.update()

	ShuffleHandle()

	BubbleSort()
	SelectionSort()
	ShellSort()
	CocktailSort()
	InsertionSort()
	PancakeSort()

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
