import numpy as np
import time
import random

def LogWrapper(func):

    def wrapper(*args, **kwargs):
        now = time.time()
        return_value = func(*args,**kwargs)
        print("Executed {0} in {1}ms".format(func.__name__, time.time()-now))
        return return_value

    return wrapper

def PrintWrapper(func):

    def wrapper(*args, **kwargs):
        print(args[1])
        return_value = func(*args, **kwargs)
        return return_value

    return wrapper

@LogWrapper
def play():
    flag = False
    board = np.array([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]])
    player = "X"
    attempt = 0
    while flag is False:
        r1 = random.randint(0, 2)
        r2 = random.randint(0, 2)
        while not board[r1][r2] == "-":
            r1 = random.randint(0, 2)
            r2 = random.randint(0, 2)
        board[r1][r2] = player
        flag = CheckWin(player, board)
        if player == "X":
            player = "O"
        else:
            player = "X"
        attempt += 1
        if attempt == 9:
            break


@PrintWrapper
def CheckWin(player, board):
    for i in range(3):
        if board[0][i] == board[1][i]== board[2][i] == player:
            return True
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if (board[0][0] == board[1][1] == board[2][2] == player) or (
                board[0][2] == board[1][1] == board[2][0] == player):
            return True
    return False

play()

