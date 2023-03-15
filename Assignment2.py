# Student name:JIFAN YAN
# Student ID: 32667965
# Student email: jyan0174@student.monash.edu
# Template for Assignment 2 - T2 2022
# Add your code below the test cases provided in each function
# Task 1
import random


def init_board():
    """
    Input: No input taken
    Output: A table that represents the 3x3 tic-tac-toe board with all the cells filled with a hyphen

    For example: 
    >>> board = init_board()
    >>> board
    [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    """
    # Add your code here
    board_lst = []
    for i in range(3):
        board_lst.append(['-','-','-'])   
    return board_lst


# Task 2
def print_board(board):
    """
    Input: The current status of the board 
    Output: Prints the current board to the screen

    For example: 
    >>> board = init_board()
    >>> print_board(board)
    -------------
    | - | - | - |
    -------------
    | - | - | - |
    -------------
    | - | - | - |
    -------------
    """
    # Add your code here
    print("-------------")
    print("| {} | {} | {} |".format(board[0][0], board[0][1], board[0][2]))

    print("-------------")
    print("| {} | {} | {} |".format(board[1][0], board[1][1], board[1][2]))

    print("-------------")
    print("| {} | {} | {} |".format(board[2][0], board[2][1], board[2][2]))

    print("-------------")


# Task 3
def is_filled(board):
    """
    Input: The current status of the board 
    Output: True if the board is filled, False otherwise

    For example: 
    >>> board = init_board()
    >>> is_filled(board)
    False
    >>> test_board = [['X','O','X'],['O','X','O'],['X','O','X']]
    >>> is_filled(test_board)
    True
    >>> test_board = [['X','O','-'],['O','X','O'],['X','-','X']]
    >>> is_filled(test_board)
    False
    """
    # Add your code here
    count_of_X = 0
    count_of_O = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                count_of_X += 1
            if board[i][j] == 'O':
                count_of_O += 1
    if count_of_O + count_of_X == 9:
        return True
    return False


# Task 4
# Add additional functions as required

def player_won(board):
    """
    Input: The current status of the board 
    Output: True if the board is filled, False otherwise

    For example: 
    >>> test_board = [['X','O','X'],['O','X','O'],['X','O','X']]
    >>> player_won(test_board)
    Congrats!! You win!
    True
    >>> test_board = [['O','X','O'],['X','O','X'],['O','X','O']]
    >>> player_won(test_board)
    I win! Nice try!
    True
    >>> test_board = [['X','-','O'],['X','-','O'],['X','-','-']]
    >>> player_won(test_board)
    Congrats!! You win!
    True
    >>> test_board = [['O','O','X'],['X','X','O'],['O','X','O']]
    >>> player_won(test_board)
    False
    """
    # we have 8 situations which are three rows, three cols and two diagonals
    # You is X
    # I is O
    winner = None  # initialize the winner
    all_X_list = ['X', 'X', 'X']
    all_O_list = ['O', 'O', 'O']
    # each row
    for row_index in range(3):
        row = []
        for i in range(3):
            row.append(board[row_index][i])# because of this board is square, so row and col can be both i
        if row == ['X', 'X', 'X']:
            winner = 'X'
        elif row == ['O', 'O', 'O']:
            winner = 'O'

    # each col
    for col_index in range(3):
        column = []
        for i in range(3):
            column.append(board[i][col_index])
        if column == ['X', 'X', 'X']:
            winner = 'X'
        elif column == ['O', 'O', 'O']:
            winner = 'O'

    # two diagonals
    left_diagonal = [board[0][0], board[1][1], board[2][2]]
    right_diagonal = [board[2][0], board[1][1], board[0][2]]


    if left_diagonal == ['X', 'X', 'X'] or right_diagonal == ['X', 'X', 'X']:
        winner = 'X'
    elif left_diagonal == ['O', 'O', 'O'] or right_diagonal == ['O', 'O', 'O']:
        winner = 'O'


    if winner == None:# no one win the game
        return False
    else:
        if winner == 'X':
            print('Congrats!! You win!')
        else:
            print("I win! Nice try!")
        return True

# Task 5


def update_board(board, row, col, player):
    """
    Input: The current status of the board, the row, column and the player (‘X’ or ‘O’) for the next move. 
    Output: True if the boa

    rd is successfully updated, False otherwise.


    For example: 
    >>> test_board = [['X','O','-'],['-','X','-'],['-','O','-']]
    >>> update_board(test_board,1,0,'X')
    True
    >>> test_board = [['X','O','-'],['-','X','-'],['X','O','-']]
    >>> update_board(test_board,2,1,'O')
    False
    """
    # Add your code here
    if (row not in [0, 1, 2]) or (col not in [0, 1, 2]):  # row and col must follow the board.
        return False
    if board[row][col] != '-':  # board[row][col] = 'X' or 'O' it will not add the 'X' and 'O' in this location
        return False
    else:
        board[row][col] = player
        return True


# Task 6
# Add additional functions as required

def get_all_possible_position(board):
    """
    Input: The current status of the board,
    Output: all possible positions for computer to choose
    """
    all_possible_position = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == '-':
                all_possible_position.append((row, col)) # the coordinates of the empty position
    return all_possible_position


def get_rows_columns_diagonals(board):
    """
    Input: The current status of the board,
    Output: 3 rows , 3 columns and 2 diagonals, with the coordinates of each point.
    """
    # 3 rows
    rows = []
    for row_index in range(3):
        tmp_row = []
        for i in range(3):
            tmp_row.append((board[row_index][i], (row_index, i)))
        rows.append(tmp_row)

        
    # 3 cols
    columns = []
    for col_index in range(3):
        tmp_col = []
        for i in range(3):
            tmp_col.append((board[i][col_index], (i, col_index)))
        columns.append(tmp_col)
    

    # 2 diagonals
    left_diagonal = []
    for i in range(3):
        left_diagonal.append((board[i][i],(i,i)))

    right_diagonal = []
    for i in range(3):
        right_diagonal.append((board[i][2-i],(i,2-i)))

    
    diagonals = [left_diagonal, right_diagonal]

    return rows, columns, diagonals


def statistics_for_list(L):
    """
    Input: A 3-length list from board,
    Output: number of X, number of O, and position of '-'
    """
    count_of_X, count_of_O = 0, 0
    pos_of_EMPTY = []
    for i in range(3):
        char = L[i][0] # this location is "X" or "O" or "-"
        pos = L[i][1] # the coordinates of location
        if char == 'X':
            count_of_X += 1
        elif char == 'O':
            count_of_O += 1
        else:
            pos_of_EMPTY.append(pos)

    return count_of_X, count_of_O,  pos_of_EMPTY


def next_move(board, level):
    """
    Input: The current status of the board and the difficulty level
    Output: Position of the next move (of the computer), as a tuple (row,column)

    For example: 
    >>> test_board = [['X','-','-'],['X','O','-'],['O','-','-']]
    >>> next_move(test_board,'hard')
    (0, 2)
    >>> test_board = [['-','X','-'],['-','X','O'],['O','-','-']]
    >>> next_move(test_board,'hard')
    (2, 1)

    """
    if level == 'easy':
        all_possible_position = get_all_possible_position(board) # with empty coordinates
        return random.choice(all_possible_position)
    elif level == 'hard':
        rows, columns, diagonals = get_rows_columns_diagonals(board) # both with coordinates
        all_list_of_board = rows + columns + diagonals

        for List in all_list_of_board:
            count_of_X, count_of_O,  pos_of_EMPTY = statistics_for_list(List)
            # If there are two ‘O’s in a row, column or a diagonal, the next move should fill the corresponding row, column or diagonal with another ‘O’ so that the computer wins.
            if count_of_O == 2 and len(pos_of_EMPTY) == 1:
                return pos_of_EMPTY[0]

        for List in all_list_of_board:
            count_of_X, count_of_O,  pos_of_EMPTY = statistics_for_list(List)
            # If there are two ‘X’ s in a row, column or a diagonal, the next move should fill the corresponding row, column or diagonal with an ‘O’ so that the computer blocks the user’s next winning move.
            if count_of_X == 2 and len(pos_of_EMPTY) == 1:
                return pos_of_EMPTY[0]

        for List in all_list_of_board:
            count_of_X, count_of_O, pos_of_EMPTY = statistics_for_list(List)
            # If there is an ‘O’ in a row, column or a diagonal, the next move should place another ‘O’ on the same row, column or diagonal.
            if count_of_O == 1 and len(pos_of_EMPTY) > 0:# avoid two "O", one "X"
                return pos_of_EMPTY[0]

        for List in all_list_of_board:
            count_of_X, count_of_O,  pos_of_EMPTY = statistics_for_list(List)
            # If there are no ‘O’s on the board, place an ‘O’ in any random available position.
            count_of_O_on_board = 0

            for row_index in range(3):
                for col_index in range(3):
                    if board[row_index][col_index] == '0':
                        count_of_O_on_board += 1

            if count_of_O_on_board == 0:
                all_possible_position = get_all_possible_position(board)
                return random.choice(all_possible_position)
# Task 7


def play():
    """
    Test this function interactively by running - ie. by playing the game
    """
    # Initialises the board
    board = init_board()
    print_board(board)
    # Lets the user choose the difficulty level and make the first move
    level = input("please choose the difficulty level, easy or hard: ")

    # first move
    first_move_x, first_move_y = map(int, input(
        "please make the first move, split as a whitespace , such as '0 2': ").split()) #read two numbers in a row

    while update_board(board, first_move_x, first_move_y, 'X') == False:
        print("You cannot select here, please select again!")
        first_move_x, first_move_y = map(int, input(
            "please make the first move, split as a whitespace , such as '0 2': ").split())
    print_board(board)
    # first move end

    now_player = 'X'

    while is_filled(board) == False and player_won(board) == False:
        now_player = 'X' if now_player == 'O' else 'O'  # change player
        if now_player == 'O':
            next_pos = next_move(board, level)
            update_board(board, next_pos[0], next_pos[1], 'O')
        else:
            player_move_x, player_move_y = map(int, input(
                "please make your move, split as a whitespace , such as '0 2': ").split())
            while update_board(board, player_move_x, player_move_y, 'X') == False:
                print("You cannot select here, please select again!")
                player_move_x, player_move_y = map(int, input(
                    "please make your move, split as a whitespace , such as '0 2': ").split())
            

        print_board(board)

    if is_filled(board) == True and player_won(board) == False:
        print("It's a tie")


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose= True)
    play()
