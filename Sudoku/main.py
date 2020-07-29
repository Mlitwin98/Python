from figures import *
from solver import Solve

p.init()
p.display.set_caption("SUDOKU")

canPlay = True
running = True
solve = False


def DisplayWin():
	global canPlay
	if val.CheckWholeBoard(squares) and not val.CheckIfEmptySpaces(squares):
		p.draw.rect(screen, lightgray, p.Rect(100, 200, 700, 500), 0)
		fontWin = p.font.SysFont('Arial', 150)
		text = fontWin.render("You won", True, black)
		text_rect = text.get_rect(center=(450, 450))
		screen.blit(text, text_rect)
		canPlay = False


while running:
	p.display.update()

	DrawSquares()
	DrawLines()
	DisplayWin()

	if solve:
		Solve(squares)

	for event in p.event.get():
		if event.type == p.QUIT:
			running = False
			p.quit()
			quit()
		elif event.type == p.MOUSEBUTTONDOWN:
			for row in range(9):
				for sq in squares[row]:
					if sq.CheckIfMouseOver():
						sq.Click()
		elif event.type == p.KEYDOWN:
			if canPlay:
				if event.key == p.K_1:
					ChangeSquareText(1)
				elif event.key == p.K_2:
					ChangeSquareText(2)
				elif event.key == p.K_3:
					ChangeSquareText(3)
				elif event.key == p.K_4:
					ChangeSquareText(4)
				elif event.key == p.K_5:
					ChangeSquareText(5)
				elif event.key == p.K_6:
					ChangeSquareText(6)
				elif event.key == p.K_7:
					ChangeSquareText(7)
				elif event.key == p.K_8:
					ChangeSquareText(8)
				elif event.key == p.K_9:
					ChangeSquareText(9)
				elif event.key == p.K_BACKSPACE:
					EraseSquareText()
				elif event.key == p.K_RETURN:
					solve = True
