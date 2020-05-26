import pygame
import random
import time

seed = random.seed()
turn = random.randint(0, 1)

# COLORS
white = (255, 255, 255)
black = (0, 0, 0)

# SHAPES
order = []
shapesPositions = []

# BOARD
possibleMoves = 9
someoneWon = False

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


def draw_circle(position):
    pygame.draw.circle(screen, black, (position[0], position[1]), 140, 5)


def draw_x(position):
    pygame.draw.line(screen, black, (position[0] - 140, position[1] - 140), (position[0] + 140, position[1] + 140), 5)
    pygame.draw.line(screen, black, (position[0] - 140, position[1] + 140), (position[0] + 140, position[1] - 140), 5)


def draw_all_shapes():
    for i in range(len(order)):
        if order[i] == 1:
            draw_x(shapesPositions[i])
        else:
            draw_circle(shapesPositions[i])


def check_if_someone_won():
    global someoneWon
    for i in range(1, 4):
        if boardCanPlace[i][1] == boardCanPlace[i][2] == boardCanPlace[i][3] != '':
            someoneWon = True
        if boardCanPlace[1][i] == boardCanPlace[2][i] == boardCanPlace[3][i] != '':
            someoneWon = True
    if boardCanPlace[1][1] == boardCanPlace[2][2] == boardCanPlace[3][3] != '':
        someoneWon = True
    if boardCanPlace[3][1] == boardCanPlace[2][2] == boardCanPlace[1][3] != '':
        someoneWon = True


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


# Start Game
pygame.init()

# Screen
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Tic-Tac-Toe")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_board()

    if possibleMoves > 0 and not someoneWon:
        random_gameplay()
        check_if_someone_won()

    draw_all_shapes()
    time.sleep(0.2)
    pygame.display.update()

print("halo")