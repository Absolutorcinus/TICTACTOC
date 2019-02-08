'''
Pyhon3.4
Tic_Tac_Toe
By IJ_Absolucrem
'''

import itertools
# **********************************************************
#  to check if the values in matrix are equal             *
# **********************************************************
'''checks if all elements in the list are equals except the 
   case where there will be equality of zeros'''
def checkEqual(m):
    if m[1:] == m[:-1]:
        if m[1]!=0:
            return m[1]
# **********************************************************
#  to check horizontal values matrix                      *
# **********************************************************
def check_horizontal_win(m):
    #print("check horizontal")
    winner = 0
    game_end=False
    for row in m:
        # print(row)
        if checkEqual(row) != None:
            winner = checkEqual(row)
            game_end=True
    return winner,game_end
# **********************************************************
#  to check vertical values transpose the original matrix *
# **********************************************************
def check_vertical_win(m):
    #print("check vertical")
    winner=0
    game_end = False
    new_matrix = [list(i) for i in zip(*m)]
    for row in new_matrix:
        # print(row)
        if checkEqual(row)!= None:
            winner =checkEqual(row)
            game_end=True
    return winner,game_end
# ********************************************************
#  to check  diagonal                                   *
# ********************************************************
def check_diagonal_win(m):
    winner = 0
    game_end=False
    #print("check diagonal")
    diagonal_1 = []
    for row in range(len(m)):
        col = row
        diagonal_1.append(m[row][col])

    if checkEqual(diagonal_1) != None:
        winner = checkEqual(diagonal_1)
        game_end = True

    diagonal_2 = []
    for row in range(len(m)):
        col = len(m) - row - 1
        diagonal_2.append(m[row][col])

    if checkEqual(diagonal_2) != None:
        winner = checkEqual(diagonal_2)
        game_end = True

    return winner,game_end
# ********************************************************
#  Print the Board                                      *
# ********************************************************
def game_board(game_map, row=0, column=0, mark=0, just_display=False):
    try:
        if not just_display:
            game_map[row][column] = mark

        print("   0  1  2")
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print("Error: input row/colums out of range!", e)

    except Exception as e:
        print("Error:", e)
# ********************************************************
#  Game checks horiz  vertic diag                        *
# ********************************************************
def game(m):
    stat=False  # status of the game: True if there is a win

    if check_horizontal_win(m)[1] == True:
        print("PLAYER ", check_horizontal_win(m)[0], "WINS!!!!")
        stat = True
    elif check_diagonal_win(m)[1]==True :
        print("PLAYER ", check_diagonal_win(m)[0], "WINS!!!!")
        stat = True
    elif check_vertical_win(m)[1]==True :
        print("PLAYER ", check_vertical_win(m)[0], "WINS!!!!")
        stat= True

    return stat
#********************************************************
play=True
players= [1,2]

while play:
    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    game_won = False
    player_choice=itertools.cycle([1,2])

    while not game_won:
        current_player=next(player_choice)
        print("****** PLAYER",current_player,"*******")
        column_choice= int(input("which column: (0,1,2)"))
        row_choice   = int(input("which row: (0,1,2)"))

#loop till the user input non-occupied cell.
        while matrix[row_choice][column_choice]!=0:

            print("Position already taken, make another choice!")
            player=current_player
            print("****** PLAYER", player, "*******")
            column_choice = int(input("which column: (0,1,2)"))
            row_choice = int(input("which row: (0,1,2)"))
            if matrix[row_choice][column_choice] == 0:
                break
        '''***********************'''
        matrix = game_board(matrix, row_choice, column_choice, current_player, False)
        a= game(matrix)
        game_won =bool(a)


        if game_won==True:
            play_again = input("do you want to paly again?:(Y/N)")
            if play_again.upper()=="Y":
                game_won=True

            elif play_again.upper()=="N":
                print("Exiting ... ")
                play=False

