from validator import *
import time as t
from figures import ChangeSquareText
val = validator()
startR = 0
startC = 0


def Backtrack(squares):
	global startC, startR
	while not squares[startR][startC].editable:
		if startC != 0:
			startC -= 1
		else:
			startR -= 1
			startC = 8
	squares[startR][startC].focused = True
	if squares[startR][startC].value + 1 > 9:
		ChangeSquareText(0)
		squares[startR][startC].focused = False
		if startC != 0:
			startC -= 1
		else:
			startR -= 1
			startC = 8
		Backtrack(squares)
	else:
		ChangeSquareText(squares[startR][startC].value + 1)


def Check(squares, num):
	global startC, startR
	if val.CheckWholeBoard(squares):
		#squares[startR][startC].focused = False
		return
	else:
		num += 1
		if num < 10:
			ChangeSquareText(num)
			Check(squares, num)
		else:
			Backtrack(squares)
		return


def Solve(squares):
	global startC, startR
	if startR < 9:
		if startC < 9:
			if squares[startR][startC].editable:
				squares[startR][startC].focused = True
				num = 1
				ChangeSquareText(num)
				Check(squares, num)
				t.sleep(0.1)
				squares[startR][startC].focused = False
			startC += 1
		else:
			startR += 1
			startC = 0
