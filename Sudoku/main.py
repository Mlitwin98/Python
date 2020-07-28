from figures import *

p.init()
p.display.set_caption("SUDOKU")

running = True
while running:
	p.display.update()
	val.CheckWholeBoard(squares)
	DrawSquares()
	DrawLines()
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
