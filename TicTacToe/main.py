import pygame
import random
import time
from tkinter import *
from tkinter import messagebox

Tk().wm_withdraw()
seed = random.seed()
turn = 0

# GLOBALS
running = True
flag = True
possibleMoves = 9
result = ''

# COLORS
white = (255, 255, 255)
black = (0, 0, 0)

# SHAPES
order = []
shapesPositions = []

# BOARD
boardPositions = [
    [(), (), (), ()],
    [(), (150, 150), (450, 150), (750, 150)],
    [(), (150, 450), (450, 450), (750, 450)],
    [(), (150, 750), (450, 750), (750, 750)]
]

boardCanPlace = [
    ['.', '.', '.', '.'],
    ['.', '', '', ''],
    ['.', '', '', ''],
    ['.', '', '', '']
]


# FUNCTIONS
def draw_board():
    screen.fill(white)
    pygame.draw.rect(screen, black, (300, 0, 1, 900))
    pygame.draw.rect(screen, black, (600, 0, 1, 900))
    pygame.draw.rect(screen, black, (0, 300, 900, 1))
    pygame.draw.rect(screen, black, (0, 600, 900, 1))


def draw_o(position):
    pygame.draw.circle(screen, black, (position[0], position[1]), 140, 5)


def draw_x(position):
    pygame.draw.line(screen, black, (position[0] - 140, position[1] - 140), (position[0] + 140, position[1] + 140), 5)
    pygame.draw.line(screen, black, (position[0] - 140, position[1] + 140), (position[0] + 140, position[1] - 140), 5)


def draw_all_shapes():
    for i in range(len(order)):
        if order[i] == 1:
            draw_x(shapesPositions[i])
        else:
            draw_o(shapesPositions[i])


def check_if_someone_won():
    for i in range(1, 4):
        if boardCanPlace[i][1] == boardCanPlace[i][2] == boardCanPlace[i][3] != '':
            if boardCanPlace[i][1] == 'x':
                return 'X', 10, True
            else:
                return 'O', -10, True
        if boardCanPlace[1][i] == boardCanPlace[2][i] == boardCanPlace[3][i] != '':
            if boardCanPlace[1][i] == 'x':
                return 'X', 10, True
            else:
                return 'O', -10, True
    if boardCanPlace[1][1] == boardCanPlace[2][2] == boardCanPlace[3][3] != '':
        if boardCanPlace[1][1] == 'x':
            return 'X', 10, True
        else:
            return 'O', -10, True
    if boardCanPlace[3][1] == boardCanPlace[2][2] == boardCanPlace[1][3] != '':
        if boardCanPlace[3][1] == 'x':
            return 'X', 10, True
        else:
            return 'O', -10, True
    return '', 0, False


def generate_random_position():
    x = random.randint(1, 3)
    y = random.randint(1, 3)
    while boardCanPlace[x][y] != '':
        x = random.randint(1, 3)
        y = random.randint(1, 3)
    return x, y


def handle_turn(x, y):
    global turn, possibleMoves, boardCanPlace
    if turn == 1:
        order.append(turn)
        shapesPositions.append(boardPositions[x][y])
        boardCanPlace[x][y] = 'x'
        possibleMoves -= 1
        turn = 0
    else:
        order.append(turn)
        shapesPositions.append(boardPositions[x][y])
        boardCanPlace[x][y] = 'o'
        possibleMoves -= 1
        turn = 1


def random_gameplay():
    position = generate_random_position()
    x = position[0]
    y = position[1]
    handle_turn(x, y)


def minimax_gameplay():
    position = find_best_move(boardCanPlace)
    x = position[0]
    y = position[1]
    handle_turn(x, y)


def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)
    for i in range(1, 4):
        for j in range(1, 4):
            if board[i][j] == '':
                board[i][j] = 'x'
                turn_f = 0
                move_val = minimax(boardCanPlace, possibleMoves - 1, turn_f)
                board[i][j] = ''
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move


def minimax(board, possible_f, turn_f):
    score = check_if_someone_won()[1]

    if score == 10 or score == -10:
        return score

    if possible_f == 0:
        return 0

    if turn_f:
        best = -10000
        for i in range(1, 4):
            for j in range(1, 4):
                if board[i][j] == '':
                    board[i][j] = 'x'
                    possible_f -= 1
                    turn_f = 0
                    best = max(best, minimax(board, possible_f, turn_f))
                    board[i][j] = ''
        return best
    else:
        best = 10000
        for i in range(1, 4):
            for j in range(1, 4):
                if board[i][j] == '':
                    board[i][j] = 'o'
                    possible_f -= 1
                    turn_f = 1
                    best = min(best, minimax(board, possible_f, turn_f))
                    board[i][j] = ''
        return best


def display_winner():
    global flag
    if (possibleMoves == 0 or check_if_someone_won()[2]) and flag:
        if result == '':
            messagebox.showinfo('Game Over', 'TIE')
        else:
            messagebox.showinfo('Game Over', f'{result[0]} WON')
        flag = False


# Start Game
pygame.init()

# Screen
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Tic-Tac-Toe")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Game Loop
while running:
    pygame.display.update()
    draw_board()
    display_winner()

    if possibleMoves > 0 and not check_if_someone_won()[2]:
        if turn:
            minimax_gameplay()
        else:
            random_gameplay()
        result = check_if_someone_won()[0]
        
    draw_all_shapes()
    time.sleep(0.3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
