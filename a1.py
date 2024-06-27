"""
CSSE1001 Assignment 1
Semester 2, 2022
"""
from a1_support import *

def num_hours() -> float:
    """
    It gives the number of hours spent on the assignment

    Returns:
        float: number of hours
    """
    return 17.0
    pass


def is_empty(position: tuple[int, int], board: Board) -> bool:
    """
    If the position on the board is None, it returns True.
    Otherwise, it returns False.

    Parameters:
        position (tuple[int, int]): First index of position is the row, second index is column.
        board (Board): The board as a list of 9 lists.

    Return:
        bool: True if position is empty, otherwise False
    """

    row = position[0]
    column = position[1]

    if bool(board[row][column]) is False:
        return True
    else:
        return False
    pass


def update_board(position: tuple[int, int], value: Optional[int], board: Board) -> None:
    """
    Updates the board with the given value, within the given position.

    Parameters:
        position (tuple[int, int]): First index of position is the row, second index is column.
        value (Optional[int]): The value with which 
        board (Board): The board as a list of 9 lists (returned from read_board() function).
    
    Precondition:
        The position must not correspond to a value on the original board.
    """
    row = position[0]
    column = position[1]

    board[row][column] = value
    pass


def clear_position(position: tuple[int, int], board: Board) -> None:
    """
    Clears the board with None within the given position.

    Parameters:
        position (tuple[int, int]): First index of position is the row, second index is column.
        board (Board): The board as a list of 9 lists (returned from read_board() function).
    
    Precondition:
        The position must not correspond to a value on the original board.
    """
    row = position[0]
    column = position[1]

    board[row][column] = None
    pass


def list_to_board(board_list: list) -> Board:
    """
    Converts a list into a list of 9 lists.
    It appends 9 columns to a list at once, and it repeats this 9 times.
    This was made into a function because it is used in read_board() and has_won() multiple times.

    Parameter:
        board_list (list): A list consisting of all the numbers on the board.

    Returns:
        Board: A list of 9 lists.
    """

    board = []

    for column in range(0,9):
        board.append(board_list[9*column:9*(column+1)])
    
    return board
    pass


def read_board(raw_board: str) -> Board:
    """
    Converts the string from load_board(filename) into a list of 9 lists.

    Parameters:
        raw_board (str): The string from load_board(filename)

    Returns:
        Board: A list of 9 lists
    """
    board_list = []

    # This loop converts each character to None or integer, and appends it to board_list. 
    for char in raw_board:
        if char == " ": 
            char = None
            board_list.append(char)
        else:
            board_list.append(int(char))

    # This converts board_list into a list of 9 lists.
    board_list_of_lists = list_to_board(board_list)

    return board_list_of_lists
    pass


def print_board(board: Board) -> None:
    """
    Converts the list of lists (board) into a user friendly format

    Parameters:
        board (Board): The list of 9 lists (created from read_board() function).
    """

    # This double 'for loop' converts each item in the board to a string, and appends it to strings_list to make one list.
    strings_list = []
    for row in board:
        for column in row:
            if column == None:
                column = " "
                strings_list.append(str(column))
            else:
                strings_list.append(str(column))

    # This combines all items in strings_list to a string.
    board_string = "".join(strings_list)

    
    # This prints each row in the required format for the user-friendly board. It prints 3 columns at a time.
    # The row variable is used to specify the row reference, and for when the HORIZONTAL_WALL and the column reference are needed.
    row = 0
    for column in range(0, 81, 9):
        print(board_string[column:column+3] + VERTICAL_WALL + board_string[column+3:column+6] + VERTICAL_WALL + board_string[column+6:column+9] + BLANK + str(row))
        row += 1
        if row == 3 or row == 6:
            print(HORIZONTAL_WALL*11)
        elif row == 9:
            print("\n012 345 678")
    pass


def row_checker(board: Board) -> bool:
    """
    Checks whether each row of the Board has 1 of each digit from 1 to 9.
    This function is used in has_won() multiple times.

    Parameter:
        board (Board): A list of 9 lists

    Returns:
        bool: Returns True if each row has 1 of each digit from 1 to 9, otherwise it returns False.
    """
    digit_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # This double 'for' loop checks each row for exactly 1 digit from digit_list.
    # If True, it adds 1 to total.
    total = 0
    for row in board:
        for number in digit_list:
            if row.count(number) == 1:
                total += 1
    
    # Total must equal 81 because that means there is 1 of each digit from 1 to 9 in each row (9 digits per row multiplied by 9 rows = 81).
    if total == 81:
        return True
    else:
        return False
    
    pass


def has_won(board: Board) -> bool:
    """
    If each column, row, and square in the sudoku board has exactly 1 of each digit from 1 to 9, it returns that the user has won.

    Parameter:
        board (Board): The list of 9 lists (created from read_board() function).

    Returns:
        bool: Returns True if there is 1 of each digit from 1 to 9 in each row, column, and square.
    """

    win_conditions = []

    # Check if each row has 1 of each digit from 1 to 9.
    row_check = row_checker(board)
    win_conditions.append(row_check)



    # Check if each column has 1 of each digit from 1 to 9.
    # This is done by first turning the columns into rows.
    transposed_list_board = []
    for column in range(9):
        for row in range(9):
            transposed_list_board.append(board[row][column])
    
    # This transposed list is converted into a board using list_to_board() so that row_checker() can check each column.
    transposed_board = list_to_board(transposed_list_board)
    column_check = row_checker(transposed_board)
    win_conditions.append(column_check)



    # Check Check if each square has 1 of each digit from 1 to 9.
    # This is done by first turning each box into a row.
    square_list_board = []
    for column in range(0, 9, 3):
        for row in board:
            square_list_board.append(row[column:column+3])
    
    # Since square_list_board is a list of 27 lists, it must be converted to one big list.
    square_full_list = []
    for row in square_list_board:
        for column in row:
            square_full_list.append(column)
    
    # square_full_list is converted to a board (with each square as a row) so that row_checker() can check each square.
    square_board = list_to_board(square_full_list)
    square_check = row_checker(square_board)
    win_conditions.append(square_check)
    


    # Checks if requirements have been met by adding the True or False booleans returned from row_checker() each time (row, column, square).
    if sum(win_conditions) == 3:
        return True
    else:
        return False

    pass



def main():
    """
    This function executes the game by combining all functions.

    The user is prompted for the directory for the board file.
    Then, the user is prompted for their move.
    User's move can either be:
        Help: Input "H" or "h"
        Quit: Input "Q" or "q"
        Updating board: Input {row} {column} {value} without the brackets.
        Clearing position: Input {row} {column} {"C"} without the brackets.
    
    Until the game has been won, the user will be prompted repeatedly for their move.
    """

    file_name = input(START_GAME_PROMPT)
    board_file = load_board(file_name)

    board_updated = read_board(board_file)
    board_original = read_board(board_file)

    # This 'while' loop repeatedly prompts user for their move until the has_won function returns True.
    while not has_won(board_updated): 

        print_board(board_updated)
        board_input = input(INPUT_PROMPT)

        # Depending on board_input, the corresponding move is executed whilst implementing the precondition.
        # The is_empty() function implements the precondition for clear_position() and update_board().

        if board_input == HELP or board_input == "h":
            print(HELP_MESSAGE+"\n")

        if board_input == QUIT or board_input == "q":
            return

        if len(board_input) == 5 and board_input[4] == CLEAR:
            row = int(board_input[0])
            column = int(board_input[2])
            if is_empty((row, column), board_original):
                clear_position((row, column), board_updated)
            else:
                print(INVALID_MOVE_MESSAGE)

            pass
        elif len(board_input) == 5:
            row = int(board_input[0])
            column = int(board_input[2])
            value = int(board_input[4])

            if is_empty((row, column), board_original):
                update_board((row, column), value, board_updated)
            else:
                print(INVALID_MOVE_MESSAGE)

    print_board(board_updated)
    print(WIN_MESSAGE)
    prompt = input(NEW_GAME_PROMPT)
    new_game_options = "yY"
    if prompt in new_game_options:
        main()
    else:
        return
    
    pass

if __name__ == "__main__":
    main()
