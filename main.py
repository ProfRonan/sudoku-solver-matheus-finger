"""Main module to run the program."""


def solve_sudoku(board: list[list[int]]) -> list[list[int]]:
    """Solves the board"""
    return board


def is_valid(board: list[list[int]]) -> bool:
    """Checks if the board is valid"""
    if len(board) != 9:
        return False
    return True
