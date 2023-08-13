import os
import random


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        while True:
            try:
                choose = int(input("pilih angka: "))
                if choose > 0 and choose < 10:
                    break
            except ValueError:
                print("input 1-9 !!!")
        col = choose // 3
        row = choose % 3 - 1
        if row == -1:
            col-=1
        if board[col][row] != "X" and board[col][row] != "O":
            break
        else:
            print("please input on null box !!!")
    board[col][row] = "O"
    draw_move(board)
    return board


def computer_move(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    while True:
        row_rand = int(random.random() * 3)
        col_rand = int(random.random() * 3)
        if board[row_rand][col_rand] != "X" and board[row_rand][col_rand] != "O":
            break
    board[row_rand][col_rand] = "X"
    
    draw_move(board)
    return board



def victory_for(board):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O" \
        or board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        print("Winner is player")
        return True
    elif board[0][0] == "X"  and board[1][1] == "X" and board[2][2] == "X"\
        or board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print("winner is computer")
        return True

    for i in range(3):
        if board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O"\
            or board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
            print("Winner is player")
            return True
        elif board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X"\
            or board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
            print("winner is computer")
            return True
    if board[0][0] != "1" and board[0][1] != "2" and board[0][2] != "3" \
        and board[1][0] != "4" and board[1][1] != "5" and board[1][2] != "6" \
            and board[2][0] != "7" and board[2][1] != "8" and board[2][2] != "9":
        print("Resault is draw")
        return True


    return False



def draw_move(board):
    # The function draws the computer's move and updates the board.
    for lop in range(3):
        print(("+" + "-"*7)*3,"+", sep="")
        print(("|" + " "*7)*3,"|", sep="")
        for i in range(3):
            print("|" + " "*3+board[lop][i]+" "*3, sep="", end="")
        print("|")
        print(("|" + " "*7)*3,"|", sep="")
    print(("+" + "-"*7)*3,"+", sep="")


#list 
var = [['1','2','3'],['4','5','6'],['7','8','9']]

while True:
    os.system('cls')
    var = computer_move(var)
    who_win = victory_for(var)
    if who_win:
        break
    var = enter_move(var)
    who_win = victory_for(var)
    if who_win:
        break





