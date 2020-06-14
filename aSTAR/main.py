import pygame
import math
from heapq import *
import time as t
import tkinter as tk
from tkinter import *

start = (1, 1)
goal = (8, 8)
board = (10, 10)

root = tk.Tk()
canvas = tk.Canvas(root, height=200, width=300)
canvas.pack()

startLabel = tk.Label(canvas, text='START', font=('Courier', 20))
goalLabel = tk.Label(canvas, text='GOAL', font=('Courier', 20))
boardLabel = tk.Label(canvas, text='BOARD', font=('Courier', 20))

x1Label = tk.Label(canvas, text='(x,y)')
x2Label = tk.Label(canvas, text='(x,y)')
x3Label = tk.Label(canvas, text='(width,height)')

startXEntry = tk.Entry(canvas, textvariable=StringVar(root, '1'), bg='#D3D3D3')
startYEntry = tk.Entry(canvas, textvariable=StringVar(root, '1'), bg='#D3D3D3')
goalXEntry = tk.Entry(canvas, textvariable=StringVar(root, '8'), bg='#D3D3D3')
goalYEntry = tk.Entry(canvas, textvariable=StringVar(root, '8'), bg='#D3D3D3')
boardWidthEntry = tk.Entry(canvas, textvariable=StringVar(root, '10'), bg='#D3D3D3')
boardHeightEntry = tk.Entry(canvas, textvariable=StringVar(root, '10'), bg='#D3D3D3')

startLabel.place(relwidth=0.3, relheight=0.1, relx=0.1, rely=0.1)
x1Label.place(relwidth=0.1, relheight=0.1, relx=0.2, rely=0.2)
startXEntry.place(relwidth=0.15, relheight=0.13, relx=0.1, rely=0.3)
startYEntry.place(relwidth=0.15, relheight=0.13, relx=0.25, rely=0.3)

goalLabel.place(relwidth=0.3, relheight=0.1, relx=0.6, rely=0.1)
x2Label.place(relwidth=0.1, relheight=0.1, relx=0.7, rely=0.2)
goalXEntry.place(relwidth=0.15, relheight=0.13, relx=0.6, rely=0.3)
goalYEntry.place(relwidth=0.15, relheight=0.13, relx=0.75, rely=0.3)

boardLabel.place(relwidth=0.3, relheight=0.1, relx=0.1, rely=0.6)
x3Label.place(relwidth=0.25, relheight=0.1, relx=0.12, rely=0.7)
boardWidthEntry.place(relwidth=0.15, relheight=0.13, relx=0.1, rely=0.8)
boardHeightEntry.place(relwidth=0.15, relheight=0.13, relx=0.25, rely=0.8)


def start_board():
	global start, goal, board
	start = (int(startXEntry.get()), int(startYEntry.get()))
	goal = (int(goalXEntry.get()), int(goalYEntry.get()))
	board = (int(boardWidthEntry.get()), int(boardHeightEntry.get()))
	root.destroy()


button = tk.Button(canvas, text='Go!', bg='red', command=start_board)
button.place(relwidth=0.3, relheight=0.2, relx=0.6, rely=0.7)

root.mainloop()

white = (255, 255, 255)
black = (0, 0, 0)
lightgray = (211, 211, 211)
blue = (173, 216, 230)
darkblue = (0, 0, 139)
red = (255, 0, 0)
green = (0, 128, 0)
pathColor = (24, 109, 245)

open_list = []
heapify(open_list)
closed_list = []

pygame.init()
WIDTH = 900
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* PathFinding")


class square:
	def __init__(self, color, x, y, isStartPoint=False, isEndPoint=False):
		self.color = color
		self.position = (x, y)
		self.parent = None
		self.rect = pygame.Rect(self.position[0] * WIDTH / board[0], self.position[1] * HEIGHT / board[1],
								WIDTH / board[0], HEIGHT / board[1])
		self.isStartPoint = isStartPoint
		self.isEndPoint = isEndPoint
		self.f = 0
		self.g = 0
		self.h = 0
		self.isBlocked = False

	def __lt__(self, other):
		return self.f < other.f

	def draw(self):
		pygame.draw.rect(screen, self.color, self.rect, 0)
		pygame.draw.rect(screen, black, self.rect, 1)

	def check(self):
		# noinspection PyArgumentList
		return self.rect.collidepoint(pygame.mouse.get_pos())

	def click(self):
		if not self.isStartPoint and not self.isEndPoint:
			self.color = black
			self.isBlocked = True

	def closeNode(self):
		if not self.isStartPoint and not self.isEndPoint:
			self.color = red

	def chooseNode(self):
		if not self.isStartPoint and not self.isEndPoint:
			self.color = green

	def calculateH(self):
		a = goal[0] - self.position[0]
		b = goal[1] - self.position[1]
		return math.sqrt(a**2 + b**2)

	def setParent(self, parent):
		self.parent = parent

	def choosePath(self):
		if not self.isStartPoint and not self.isEndPoint:
			self.color = pathColor


# Fill lists with squares
squares = [[square(red, 0, 0) for i in range(board[0])] for j in range(board[1])]
for i in range(board[0]):
	for j in range(board[1]):
		if i == start[0] and j == start[1]:
			squares[i][j] = square(darkblue, i, j, True)
			heappush(open_list, (0, squares[i][j]))
		elif i == goal[0] and j == goal[1]:
			squares[i][j] = square(darkblue, i, j, isEndPoint=True)
		else:
			squares[i][j] = square(white, i, j)


def startSearch():
	global search, displayPath

	f, currentSquare = heappop(open_list)
	closed_list.append(currentSquare)
	currentSquare.chooseNode()
	pygame.display.update()

	if currentSquare.isEndPoint:
		displayPath = True
		search = False
		return currentSquare

	for adjacent in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

		if currentSquare.position[0] + adjacent[0] < 0 or currentSquare.position[0] + adjacent[0] == board[0] or \
				currentSquare.position[1] + adjacent[1] < 0 or currentSquare.position[1] + adjacent[1] == board[1]:
			continue

		childSquare = squares[currentSquare.position[0] + adjacent[0]][currentSquare.position[1] + adjacent[1]]

		if childSquare.isBlocked:
			continue

		if childSquare in closed_list:
			continue

		moveCost = 1
		if adjacent[0] != 0 and adjacent[1] != 0:
			moveCost = 1.5

		possibleG = currentSquare.g + moveCost

		if (childSquare.f, childSquare) in open_list and possibleG > childSquare.g:
			continue

		childSquare.g = currentSquare.g + moveCost
		childSquare.h = childSquare.calculateH()
		childSquare.f = childSquare.g + childSquare.h
		childSquare.parent = currentSquare

		heappush(open_list, (childSquare.f, childSquare))
		childSquare.closeNode()
		pygame.display.update()


# State variables for pygame
running = True
colorSquares = False
search = False
displayPath = False

while running:
	pygame.display.update()
	screen.fill(lightgray)
	for row in squares:
		for square in row:
			square.draw()

	if colorSquares:
		for row in squares:
			for square in row:
				if square.check():
					square.click()

	if search and len(open_list) > 0:
		finish = startSearch()

	if displayPath and not finish.isStartPoint:
		finish.choosePath()
		finish = finish.parent
		pygame.display.update()
		t.sleep(0.2)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			quit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			colorSquares = True
		elif event.type == pygame.MOUSEBUTTONUP:
			colorSquares = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				search = True
