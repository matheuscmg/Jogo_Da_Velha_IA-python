from ast import While, main
from json.encoder import INFINITY
from multiprocessing import Value
from turtle import pos
import numpy as np
from enum import Enum
from colorama import Fore


class Players(Enum):
    playerOne = 'O'
    IA = 'X'


def checkDraw(board):
    for i in range(0, 3):
        for j in range(0, 3):
            if (board[i][j] == ' '):
                return False
    return True


def hoWin(mark):
    if (board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == mark):
        return True
    elif (board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] == mark):
        return True
    elif (board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] == mark):
        return True
    elif (board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] == mark):
        return True
    elif (board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] == mark):
        return True
    elif (board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] == mark):
        return True
    elif (board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == mark):
        return True
    elif (board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[2][0] == mark):
        return True
    else:
        return False


def minimax(board, depth, isMaximizing):
    if (hoWin(Players.IA.value)):
        return 1
    elif (hoWin(Players.playerOne.value)):
        return - 1
    elif (checkDraw(board)):
        return 0

    if (isMaximizing):
        bestScore = - 1500
        for i in range(0, 3):
            for j in range(0, 3):
                if (board[i][j] == ' '):
                    board[i][j] = Players.IA.value
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    if (score > bestScore):
                        bestScore = score
        return bestScore
    else:
        bestScore = 1500
        for i in range(0, 3):
            for j in range(0, 3):
                if (board[i][j] == ' '):
                    board[i][j] = Players.playerOne.value
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    if (score < bestScore):
                        bestScore = score
        return bestScore


def bestMove(board):
    bestScore = - 1500
    bestMove = []

    for i in range(0, 3):
        for j in range(0, 3):
            if (board[i][j] == ' '):
                board[i][j] = Players.IA.value
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if (score > bestScore):
                    bestScore = score
                    bestMove = [i, j]
    insertGame(bestMove[0], bestMove[1], 2)
    return


def isPlaceIsEmptyForPlay(line, column):
    return True if board[line][column] == ' ' else False


def changePlayerTime(player):
    return 1 if player == 2 else 2


def isValidValueForPlay(line, column):
    return True if line <= 2 and column <= 2 and line >= 0 and column >= 0 else False


def insertGame(line, column, player):
    if (player == 1):
        board[line][column] = Players.playerOne.value
    else:
        board[line][column] = Players.IA.value


def displayGame(board):
    print(Fore.LIGHTMAGENTA_EX + "    0     1    2\n" + Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX +"0:    " + Fore.RESET + Fore.BLUE + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("    -------------")
    print(Fore.LIGHTMAGENTA_EX + "1:    " +Fore.RESET + Fore.BLUE + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("    -------------")
    print(Fore.LIGHTMAGENTA_EX + "2:    " +Fore.RESET + Fore.BLUE + board[2][0] + " | " + board[2][1] + " | " + board[2][2])


def startGame(player):
    while True:

        if (hoWin(Players.playerOne)):
            print(f'Congratulations for the player 2 for win the game!')
            break

        if (hoWin(Players.IA.value)):
            print(f'Congratulations for the IA to win the game!')
            break

        if (checkDraw(board)):
            print('\n(Draw Game!)')
            break

        player = changePlayerTime(player)

        if (player == 1):
            print(Fore.CYAN + 'AI thinking about the movement..\n')
            bestMove(board)
            continue

        displayGame(board)
        print()
        if (player == 2):
            print(Fore.YELLOW + f'\nWelcome player {player-1} make your play' + Fore.RESET)
            try:
                line = int(input('enter line : '))
                column = int(input('enter column : '))

                if (not isValidValueForPlay(line, column)):
                    print('Line or column invalid')
                    continue

                if (not isPlaceIsEmptyForPlay(line, column)):
                    print('Position has already been filled or line or column invalid')
                    player = changePlayerTime(player)
                    continue
                insertGame(line, column, 1)
            except:
                print('Invalid charter')
                player = changePlayerTime(player)


if __name__ == '__main__':
    print(Fore.LIGHTRED_EX + '---------------------------')
    print('Welcome to the game')
    print('---------------------------' + Fore.RESET)
    player = 2
    board = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
    startGame(player)
    print('(Finish the game!)\n')
    displayGame(board)
