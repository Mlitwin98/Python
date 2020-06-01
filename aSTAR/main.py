import pygame

white = (255, 255, 255)
black = (0, 0, 0)
lightgray = (211, 211, 211)
blue = (173, 216, 230)
darkblue = (0, 0, 139)

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("A* PathFinding")


class square:
	def __init__(self, color, x, y, isStartPoint=False, isEndPoint=False):
		self.color = color
		self.x = x
		self.y = y
		self.rect = pygame.Rect(x, y, 20, 20)
		self.isStartPoint = isStartPoint
		self.isEndPoint = isEndPoint

	def draw(self):
		pygame.draw.rect(screen, self.color, self.rect, 0)
		pygame.draw.rect(screen, black, self.rect, 1)

	def check(self):
		return self.rect.collidepoint(pygame.mouse.get_pos())

	def click(self):
		if not self.isStartPoint and not self.isEndPoint:
			self.color = blue


running = True
colorSquares = False

squares = []
for i in range(41):
	for j in range(41):
		if i == j == 1:
			squares.append(square(darkblue, i*20, j*20, True))
		elif i == j == 38:
			squares.append(square(darkblue, i * 20, j * 20, isEndPoint=True))
		else:
			squares.append(square(white, i*20, j*20))

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
