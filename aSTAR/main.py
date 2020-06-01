import pygame

white = (255, 255, 255)
black = (0, 0, 0)
lightgray = (211, 211, 211)
blue = (173, 216, 230)

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("A* PathFinding")


class square:
	def __init__(self, color, x, y):
		self.color = color
		self.x = x
		self.y = y

	def draw(self):
		pygame.draw.rect(screen, self.color, (self.x, self.y, 20, 20), 0)
		pygame.draw.rect(screen, black, (self.x, self.y, 20, 20), 1)

	def isOver(self, mouse):
		if self.x < mouse[0] < self.x + 20 and self.y < mouse[1] < self.y + 20:
			return True
		return False

	def click(self):
		self.color = blue
		self.draw()


running = True

squares = []
for i in range(41):
	for j in range(41):
		squares.append(square(white, i*20, j*20))

while running:
	pygame.display.update()
	screen.fill(lightgray)
	for i in range(len(squares)):
		squares[i].draw()

	for event in pygame.event.get():
		pos = pygame.mouse.get_pos()

		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			quit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			for i in range(len(squares)):
				if squares[i].isOver(pos):
					squares[i].click()
