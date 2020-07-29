from validator import *
import time as t
from figures import ChangeSquareText
val = validator()
startR = 0
startC = 0


def Check(squares, num):
	global startC, startR
	if val.CheckWholeBoard(squares):
		squares[startR][startC].focused = False
		return True
	else:
		num += 1
		ChangeSquareText(num)
		Check(squares, num)
		return True


def Solve(squares):
	global startC, startR
	if startR < 9:
		if startC < 9:
			if squares[startR][startC].value == 0:
				print(startR, startC)
				squares[startR][startC].focused = True
				num = 1
				ChangeSquareText(num)
				Check(squares, num)
				startC += 1
				t.sleep(0.5)
		else:
			startR += 1
			startC = 0
