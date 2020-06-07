import pygame
import math

white = (255, 255, 255)
black = (0, 0, 0)
lightgray = (211, 211, 211)
blue = (173, 216, 230)
darkblue = (0, 0, 139)
red = (255, 0, 0)
green = (0, 128, 0)

start = (1, 1)
goal = (38, 38)

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("A* PathFinding")


class square:
	def __init__(self, color, x, y, isStartPoint=False, isEndPoint=False):
		self.color = color
		self.x = x
		self.y = y
		self.rect = pygame.Rect(self.x * 20, self.y * 20, 20, 20)
		self.isStartPoint = isStartPoint
		self.isEndPoint = isEndPoint
		self.parentX = -1
		self.parentY = -1
		self.f = 1000
		self.g = 1000
		self.h = 1000
		self.isBlocked = False

	def draw(self):
		pygame.draw.rect(screen, self.color, self.rect, 0)
		pygame.draw.rect(screen, black, self.rect, 1)

	def check(self):
		return self.rect.collidepoint(pygame.mouse.get_pos())

	def click(self):
		if not self.isStartPoint and not self.isEndPoint:
			self.color = blue
			self.isBlocked = True

	def closeNode(self):
		if not self.isStartPoint and not self.isEndPoint:
			self.color = red

	def chooseNode(self):
		if not self.isStartPoint and not self.isEndPoint:
			self.color = green

	def calculateH(self):
		a = goal[0] - self.x
		b = goal[1] - self.y
		return math.sqrt(a*a + b*b)


running = True
colorSquares = False

squares = []
for i in range(41):
	for j in range(41):
		if i == start[0] and j == start[1]:
			squares.append(square(darkblue, i, j, True))
		elif i == goal[0] and j == goal[1]:
			squares.append(square(darkblue, i, j, isEndPoint=True))
		else:
			squares.append(square(white, i, j))

while running:
	pygame.display.update()
	screen.fill(lightgray)
	for i in range(len(squares)):
		squares[i].draw()

	if colorSquares:
		for i in range(len(squares)):
			if squares[i].check():
				squares[i].click()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			quit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			colorSquares = True
		elif event.type == pygame.MOUSEBUTTONUP:
			colorSquares = False
