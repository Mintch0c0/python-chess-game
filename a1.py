"""
Chess Game
Supplementary Assessment
CSSE1001
The University of Queensland 2024
"""

from typing import Optional, Tuple

from a1_support import *

# Replace these <strings> with your name, student number and email address.
__author__ = "Febriani Patricia, 48914127"
__email__ = "s4891412@uq.edu.au"

# Write your functions here

def initial_state() -> Board:
    """
    The initial state of board.

    Returns:
        Board: an octuple strings (Each of the eight strings corresponds
        to a row on the chess board, with each character within the string
        denoting either a chess piece or an empty square.)
    """
    
    return (
        f"{BLACK_ROOK}{BLACK_KNIGHT}{BLACK_BISHOP}{BLACK_QUEEN}{BLACK_KING}{BLACK_BISHOP}{BLACK_KNIGHT}{BLACK_ROOK}",
        f"{BLACK_PAWN * 8}",
        f"{EMPTY * 8}",
        f"{EMPTY * 8}",
        f"{EMPTY * 8}",
        f"{EMPTY * 8}",
        f"{WHITE_PAWN * 8}",
        f"{WHITE_ROOK}{WHITE_KNIGHT}{WHITE_BISHOP}{WHITE_QUEEN}{WHITE_KING}{WHITE_BISHOP}{WHITE_KNIGHT}{WHITE_ROOK}"
    )

def print_board(board: Board) -> None:
    """
    Displaying the chess board.

    Precondition:
         The row and its number are separated by two spaces, while there
         is a single empty line between the board and the row of letters abcdefgh.
    """
    i = 0
    while i < 8:
        print(f"{board[i]} {8 - i}") #separated by 2 spaces
        i += 1
    print("\nabcdefgh") #separated by an empty line

def square_to_position(square: str) -> Position:
    """
    Change a chess square notation into a tuple that shows the row and column of the square.

    Parameter:
        square (str): A string representing the square

    preconditions:
        The position (0, 0) corresponds to the top-left corner of the board (a8)
        The position (7, 0) corresponds to the bottom-left corner of the board (a1)
    """
    column = 'abcdefgh'
    return (8 - int(square[1]), column.index(square[0].lower()))

def process_move(user_input: str) -> Move:
    """
    Processes the user's input for a piece movement

    Parameter:
        user_input (str): A string to initiate a movement, for example "h1 h3"

    Returns:
        Move: Tuple[Position, Position], representing before and after move.
    """
    first_position, second_position = user_input.split()
    return (square_to_position(first_position), square_to_position(second_position))

def change_position(board: Board, position: Position, character: str) -> Board:
    """
    Returns an updated copy of the board with the specified character placed
    at the given position on the chess board.

    Parameters:
        board (Board): A tuple of 8 strings, each representing a row of the chess board.
        position (Position): A tuple of two integers (row,coloumn) indicating the target position.
        character (str): chess piece
    """
    row = position[0]
    column = position[1]
    current_row = board[row]
    
    # Generates a new row with the character modified at the designated position.
    changed_row = current_row[:column] + character + current_row[column + 1:]
    
    # Generates a new board with the updated row
    return (board[:row] + (changed_row,) + board[row + 1:])

def clear_position(board: Board, position: Position) -> Board:
    """
    Removes the piece at the specified position

    Parameters:
        board (Board): A tuple of 8 strings representing rows of the chess board.
        position (Position): A tuple of two integer (row,column)

    Returns:
        Board: the updated chess board.
    """
    row = position[0]
    column = position[1]
    current_row = board[row]
    
    # Change a piece into empty
    cleared_row = current_row[:column] + EMPTY + current_row[column + 1:]
    return board[:row] + (cleared_row,) + board[row + 1:]

def update_board(board: Board, move: Move) -> Board:
    """
    Assumes the move is valid and returns the board with the move applied.

    Parameters:
        board (Board): A tuple of 8 strings representing rows of the chess board.
        move (Move): A tuple of two Position tuples (before, after) 

    Returns:
        Board: the updated chess board.
    """
    
    row_before, column_before = move[0]
    piece = board[row_before][column_before]
    board = clear_position(board, move[0])
    # update position
    board = change_position(board, move[1], piece)
    
    return board

def is_current_players_piece(piece: str, whites_turn: bool) -> bool:
    """

    Parameters:
        piece (str): represents a chess piece.
        whites_turn (bool): True if it is white's turn.

    Returns:
        bool: If the piece is owned by the player whose turn it is, then
        the statement is true; otherwise, it is false.
    """
    if whites_turn:
        return piece in WHITE_PIECES
    else:
        return piece in BLACK_PIECES

def is_move_valid(move: Move, board: Board, whites_turn: bool) -> bool:
    """
    Returns True only if the move is valid for the current player's turn based on the current board state.

    Preconditions:
        Both positions in the move must be exist on the board.
        The before and after positions must be different.
        The piece being moved must belong to the current player.
        The destination square must be either empty or occupied by an opponent's piece.
        The move must comply with the movement rules of the piece being moved (e.g., a rook cannot move diagonally).
        The move must not place the current player in check.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    position_before, position_after = move
    
    # Ensure that both positions are exist on the board.
    if out_of_bounds(position_before) or out_of_bounds(position_after):
        return False
    
    # Ensure that the positions in the move are different.
    if position_before == position_after:
        return False
    
    piece = board[position_before[0]][position_before[1]]
    
    # Check if the piece belongs to the current player.
    if (whites_turn and piece not in WHITE_PIECES) or (not whites_turn and piece not in BLACK_PIECES):
        return False
    
    # Check if the move is valid based on the chess rules
    if position_after not in get_possible_moves(position_before, board):
        return False

    # Ensure that the move does not put the player whose turn it is in check
    dummy_board = [list(row) for row in board]
    dummy_board[position_after[0]][position_after[1]] = dummy_board[position_before[0]][position_before[1]]
    dummy_board[position_before[0]][position_before[1]] = EMPTY

    if is_in_check(dummy_board, whites_turn):
        return False
    
    return True


def can_move(board: Board, whites_turn: bool) -> bool:
    """
    Returns True only if the player can make a valid move without putting themselves in check.

    Parameters:
        board (Board): A tuple of 8 strings representing board's rows.
        whites_turn (bool): True if it is white's turn.

    Returns:
        bool: True if the player can make a valid move, False otherwise.
    """
    for row_index, row in enumerate(board):
        for col_index, piece in enumerate(row):
            if is_current_players_piece(piece, whites_turn):
                for move in get_possible_moves((row_index, col_index), board):
                    if not is_in_check(update_board(board, ((row_index, col_index), move)), whites_turn):
                        return True
    return False


def is_stalemate(board: Board, whites_turn: bool) -> bool:
    """
    Parameters:
        board (Board): A tuple of 8 strings representing board's rows.
        whites_turn (bool): True if it is white's turn.

    Returns:
        bool: True if it is stalemate, False otherwise.

    Preconditions:
        Occurs when the player, who is not currently in check,
        finds themselves unable to make a move without placing themselves in check.
    """
    # Check if the player is not in check
    player_in_check = is_in_check(board, whites_turn)
    
    # Check if the player can make any valid move
    player_can_move = can_move(board, whites_turn)
    
    # A stalemate occurs
    if not player_in_check and not player_can_move:
        return True
    return False


def check_game_over(board: Board, whites_turn: bool) -> bool:
    """
    precondition:
        happend due to stalemate or checkmate

    Returns:
        bool: True if the game is over, False otherwise.
        print the result of the game
    """
    if is_in_check(board, whites_turn):
        player_turn = "White" if whites_turn else "Black"
        if not can_move(board, whites_turn):
            print("Checkmate")
            return True
        else:
            print(f"{player_turn} is in check")
    elif is_stalemate(board, whites_turn):
        print("Stalemate")
        return True
    return False

def attempt_promotion(board: Board, whites_turn: bool) -> Board:
    """
    precondition:
        This function determines whether a pawn on the board needs to be promoted.
        In such a case, it asks the user to pick a replacement piece,
        makes the necessary changes to the board, and returns the updated version.

    Returns:
        Board: board after promotion
    """
    pieces = {
        'q': WHITE_QUEEN if whites_turn else BLACK_QUEEN,
        'n': WHITE_KNIGHT if whites_turn else BLACK_KNIGHT,
        'r': WHITE_ROOK if whites_turn else BLACK_ROOK,
        'b': WHITE_BISHOP if whites_turn else BLACK_BISHOP
    }

    if whites_turn:
        row = 0
    else:
        row = 7

    for col, piece in enumerate(board[row]):
        if (whites_turn and piece == WHITE_PAWN) or (not whites_turn and piece == BLACK_PAWN):
            print(f"What piece would you like (q, n, r, b)? ", end='')
            while True:
                answer = input().lower()
                if answer in pieces:
                    board = change_position(board, (row, col), pieces[answer])
                    return board
                print("Invalid input. Please enter q, n, r, or b.")
    return board


def is_valid_castle_attempt(move: Move, board: Board, whites_turn: bool, castling_info: Tuple[bool, bool, bool]) -> bool:
    """
    Parameters:
        move (Move): player's valid move.
        board (Board): The current board state.
        whites_turn (bool): True if it is white's turn.
        castling_info (Tuple[bool, bool, bool]): A tuple of booleans indicating whether the player's left rook,
        king, and right rook have moved during the game, respectively.

    Returns:
        bool: True if the given move is a valid attempt at castling, False otherwise.
    """
    (king_row, king_col), (rook_row, rook_col) = move

    # move of the king
    if (king_row, abs(king_col - rook_col))!= (rook_row, 2):
        return False

    # move of the rook
    if (king_col > rook_col and (whites_turn and castling_info[2] or not whites_turn and castling_info[2])) or (king_col < rook_col and (whites_turn and castling_info[0] or not whites_turn and castling_info[0])):
        return False

    # Ensure no pieces are between the king and the rook
    if king_col > rook_col:
        for col in range(rook_col + 1, king_col):
            if piece_at_position((king_row, col), board)!= EMPTY:
                return False
    else:
        for col in range(king_col + 1, rook_col):
            if piece_at_position((king_row, col), board)!= EMPTY:
                return False

    # Verify the king would not be in check after castling
    dummy_board = [list(row) for row in board]
    dummy_board[king_row][king_col], dummy_board[king_row][rook_col] = dummy_board[king_row][rook_col], dummy_board[king_row][king_col]
    if is_in_check(tuple(map(tuple, dummy_board)), whites_turn):
        return False

    return True

def perform_castling(move: Move, board: Board) -> Board:
    """
    Returns:
        Board: The updated board state after the castling move.
    """
    (king_start_row, king_start_col), (king_end_row, king_end_col) = move

    # Identify if it's a king-side or queen-side castling
    king = king_end_col - king_start_col == 2
    rook_start_col = 7 if king else 0
    rook_end_col = 5 if king else 3

    # Move the king to the new position
    king_piece = BLACK_KING if king_start_row == 0 else WHITE_KING
    updated_board = change_position(board, (king_start_row, king_start_col), EMPTY)
    updated_board = change_position(updated_board, (king_end_row, king_end_col), king_piece)

    # Move the rook to the new position
    rook_start = (king_start_row, rook_start_col)
    rook_end = (king_start_row, rook_end_col)
    rook_piece = BLACK_ROOK if king_start_row == 0 else WHITE_ROOK
    updated_board = change_position(updated_board, rook_start, EMPTY)
    updated_board = change_position(updated_board, rook_end, rook_piece)

    return updated_board

def is_valid_en_passant(move: Move, board: Board, whites_turn: bool, en_passant_position: Optional[Position]) -> bool:
    """
    Parameters:
        move (Move): Player's valid move
        board (Board): The current state of the chess board.
        whites_turn (bool): True if it is white's turn.
        en_passant_position (Optional[Position]): Represents the position skipped
        by the opponent's pawn, or None if a pawn did not move forward two positions on the last move.

    Returns:
        bool: True if the move is a valid en passant move, otherwise False.
    """
    before, after = move

    total_difference = 0
    for i in range(len(before)):
        total_difference += abs(before[i] - after[i])
    if total_difference != 2:
        return False

    if after != en_passant_position:
        return False

    if whites_turn and after[0] != before[0] - 1:
        return False
    if not whites_turn and after[0] != before[0] + 1:
        return False

    return True

def perform_en_passant(move: Move, board: Board, whites_turn: bool) -> Board:
    """
    Returns:
        Board: updated board after the en passant move is performed.
    """
    ((row_before, col_before), (row_after, col_after)) = move

    updated_board = [list(row) for row in board]
    updated_board[row_after][col_after] = WHITE_PAWN if whites_turn else BLACK_PAWN
    updated_board[row_before][col_before] = EMPTY

    # Remove the captured pawn
    updated_board[row_after + (-1 if not whites_turn else 1)][col_after] = EMPTY
    updated_board = tuple(''.join(row) for row in updated_board)

    return updated_board



def update_castling_info(move: Move, whites_turn: bool, castling_info: Tuple[bool, bool, bool]) -> Tuple[bool, bool, bool]:
    """
    Update the castling rights information based on the player's move.

    Args:
        move (Move): Player's valid move
        whites_turn (bool): True if it is white's turn.
        castling_info (Tuple[bool, bool, bool]): The current castling information

    Returns:
        Tuple[bool, bool, bool]: Updated castling information.
    """
    row, col = move[0]

    has_moved = True
    left_rook, right_rook = (col == 6, col == 6) if col == 6 else (True, castling_info[2])

    return (left_rook, has_moved, right_rook)


def update_en_passant_position(move: Move, board: Board, whites_turn: bool) -> Optional[Position]:
    """
    Update the en passant position based on the player's move.

    Args:
        move (Move): Player's valid move
        board (Board): The current state of the chess board.
        whites_turn (bool): True if it is white's turn.

    Returns:
        If the current player's pawn just advanced two squares,
        returns the position where an opponent's pawn could capture
        it with a valid en passant move.

        If an en passant move is not possible, returns None.
    """
    (row_before, col_before), (row_after, col_after) = move

    if abs(row_before - row_after) == 2:
        movement_row = (row_before + row_after) // 2
        return (movement_row, col_before)

    return None

def main():
    """
        Displaying the gameplay
    """
    board = initial_state()
    whites_turn = True
    game_over = False

    while not game_over:
        print_board(board)
        if whites_turn:
            player_turn = "White"
        else:
            player_turn = "Black"

        if is_in_check(board, whites_turn) and not can_move(board, whites_turn):
            print("Checkmate\n")
            game_over = True
        elif is_in_check(board, whites_turn):
            print("\n"f"{player_turn} is in check")
            valid_move = False
            while not valid_move:
                user_input = input("\n"f"{player_turn}'s move: ")
                if len(user_input)!= 5 or user_input[2]!= ' ':
                    print("Invalid move\n")
                    print_board(board)
                else:
                    col_before = user_input[0].lower()
                    row_before = int(user_input[1])
                    col_after = user_input[3].lower()
                    row_after = int(user_input[4])

                    if col_before not in 'abcdefgh' or col_after not in 'abcdefgh':
                        print("Invalid move\n")
                        print_board(board)
                    elif row_before not in range(1, 9) or row_after not in range(1, 9):
                        print("Invalid move\n")
                        print_board(board)
                    else:
                        move = process_move(user_input)
                        if is_move_valid(move, board, whites_turn):
                            board = update_board(board, move)
                            valid_move = True
                        else:
                            print("Invalid move\n")
                            print_board(board)
        elif is_stalemate(board, whites_turn):
            print("Stalemate\n")
            game_over = True
        else:
            valid_move = False
            while not valid_move:
                user_input = input("\n"f"{player_turn}'s move: ")

                if user_input.lower() == 'h':
                    print(HELP_MESSAGE)
                    print_board ( board )
                elif user_input.lower() == 'q':
                    want_quit = input(f"Are you sure you want to quit? ")
                    if want_quit.lower() == 'y':
                        game_over = True
                        valid_move = True
                    else:
                        valid_move = True
                else:
                    if len(user_input)!= 5 or user_input[2]!= ' ':
                        print("Invalid move\n")
                        print_board(board)
                    else:
                        col_before = user_input[0].lower()
                        row_before = int(user_input[1])
                        col_after = user_input[3].lower()
                        row_after = int(user_input[4])

                        if col_before not in 'abcdefgh' or col_after not in 'abcdefgh':
                            print("Invalid move\n")
                            print_board(board)
                        elif row_before not in range(1, 9) or row_after not in range(1, 9):
                            print("Invalid move\n")
                            print_board(board)
                        else:
                            move = process_move(user_input)
                            if is_move_valid(move, board, whites_turn):
                                board = update_board(board, move)
                                valid_move = True
                            else:
                                print("Invalid move\n")
                                print_board(board)

        if not game_over and not (user_input.lower() == 'q' and want_quit.lower()!= 'y'):
            whites_turn = not whites_turn

if __name__ == "__main__":
    main()
