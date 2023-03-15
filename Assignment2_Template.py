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
    # Try to use list comprehension for most of the list
    return [['-', '-', '-'] for i in range(3)]


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
    x = "-------------"
    print(x)
    for i in range(3):
        print("| " + board[i][0] + " | " + board[i][1] + " | " + board[i][2] + " |\n" + x)


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
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                return False
    return True


# Task 4
# Add additional functions as required
# The following additional functions is seperated as I use it to test for both player and the computer scenario

def check_win(board,ltr):
    placementx = [[i, j] for j in range(3) for i in range(3) if board[i][j] == ltr]
    for i in range(3):
        # Check for horizontal and vertical win
        if [0, i] in placementx and [1, i] in placementx and [2, i] in placementx:
            return True
        elif [i, 0] in placementx and [i, 1] in placementx and [i, 2] in placementx:
            return True
    # Check for diagonal win
    if [1, 1] in placementx:
        if [0, 0] in placementx and [2, 2] in placementx:
            return True
        elif [2, 0] in placementx and [0, 2] in placementx:
            return True
    else:
        # Only return false when all scenario above is false
        return False


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

    player = check_win(board, "X")
    computer = check_win(board, "O")
    if player:
        print("Congrats!! You win!")
        return True
    if computer:
        print("I win! Nice try!")
        return True
    else:
        return False


# Task 5
def update_board(board, row, col, player):
    """
    Input: The current status of the board, the row, column and the player (‘X’ or ‘O’) for the next move. 
    Output: True if the board is successfully updated, False otherwise.


    For example: 
    >>> test_board = [['X','O','-'],['-','X','-'],['-','O','-']]
    >>> update_board(test_board,1,0,'X')
    True
    >>> test_board = [['X','O','-'],['-','X','-'],['X','O','-']]
    >>> update_board(test_board,2,1,'O')
    False
    """
    if board[row][col] == "-":
        board[row][col] = player
        return True
    else:
        return False


# Task 6
# Add additional functions as required

# Compare if there is win condition and check if the block is empty,
# Immediately break when found
def check_chance(board, player):
    placementx = [[i, j] for j in range(3) for i in range(3) if board[i][j] == player]

    for i in range(3):
        if ([0, i] in placementx and [1, i] in placementx):
            answer = (2, i)
            break
        elif ([1, i] in placementx and [2, i] in placementx):
            answer = (0, i)
            break
        elif ([0, i] in placementx and [2, i] in placementx):
            answer = (1, i)
            break
        elif ([i, 0] in placementx and [i, 1] in placementx):
            answer = (i, 2)
            break
        elif ([i, 1] in placementx and [i, 2] in placementx):
            answer = (i, 0)
            break
        elif ([i, 0] in placementx and [i, 2] in placementx):
            answer = (i, 1)
            break
        elif ([0, 0] in placementx and [2, 2] in placementx) or ([0, 0] in placementx and [2, 2] in placementx):
            answer = (1, 1)
            break
        elif ([1, 1] in placementx and [2, 2] in placementx):
            answer = (0, 0)
            break
        elif ([1, 1] in placementx and [0, 0] in placementx):
            answer = (2, 2)
            break
        elif ([2, 0] in placementx and [1, 1] in placementx):
            answer = (0, 2)
            break
        elif ([0, 2] in placementx and [1, 1] in placementx):
            answer = (2, 0)
            break
        else:
            answer = None

    if answer != None:
        if board[answer[0]][answer[1]] != "-":
            answer = None
    return answer

# Function to find the diagonal or same row or same column of choice
def find_opposite(board, player):
    placementx = [[i, j] for j in range(3) for i in range(3) if board[i][j] == player]
    candidate = [0, 1, 2]
    for i in placementx:
        if board[i[1]][i[0]] == "-":
            return (i[1], i[0])
        elif board[2 - i[0]][2 - i[1]] == "-":
            return (2 - i[0], 2 - i[1])
        else:
            for j in candidate:
                if board[j][i[1]] == "-":
                    return (j, i[1])
                elif board[i[0]][j] == "-":
                    return (i[0], j)
    return None


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
    # Collect All empty choice
    lstempty = [(a, i) for a in range(3) for i in range(3) if board[a][i] == "-"]

    # Easy mode
    if level == "Easy":
        return random.choice(lstempty)
    else:
        comp_choice = check_chance(board, "O")
        if comp_choice != None:
            return comp_choice
        comp_choice = check_chance(board, "X")
        if comp_choice is not None:
            return comp_choice
        comp_choice = find_opposite(board, "O")
        if comp_choice != None:
            return comp_choice
        else:
            return random.choice(lstempty)


# Task 7
def play():
    """
    Test this function interactively by running - ie. by playing the game
    """

    board = init_board()
    print("would you like to play in easy or hard mode? E for easy and H for hard")
    difficulty = input()
    difficulty = difficulty.upper()
    if difficulty == "E":
        difficulty = "Easy"
    else:
        difficulty = "Hard"
    # Loop when the no one won and the board still have place to fill
    while not is_filled(board) and not player_won(board):
        player = False
        print_board(board)
        while not player:
            print("pick where you want to put your X. enter x-axis,press enter, enter y-axis,press enter")
            xaxis = input()
            yaxis = input()
            if 0 <= xaxis < 3 and 0 <= yaxis < 3:
                player = update_board(board, xaxis, yaxis, "X")
        mymove = next_move(board, difficulty)
        update_board(board, mymove[0], mymove[1], "O")
        print_board(board)
    if is_filled(board) and not player_won(board):
        print("It is a tie")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    play()
