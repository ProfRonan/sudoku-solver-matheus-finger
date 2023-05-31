"""Test file for testing the functions in main.py file"""

import unittest  # for creating the test case
import sys  # for adding the parent directory to the path
from pathlib import Path  # for getting the path of the main.py file
# add the parent directory to the path in order to run it from the run command in vscode
MAIN_FILE_FOLDER = Path(__file__).parents[1]
sys.path.insert(1, str(MAIN_FILE_FOLDER))
from main import is_valid, solve_sudoku  # nopep8 pylint: disable=wrong-import-position, import-error


class TestSudoku(unittest.TestCase):
    """Class for testing the main.py file"""

    def setUp(self):
        """Set up the test case"""
        self.boards = []

        puzzle = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        solution = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        self.boards.append({"puzzle": puzzle, "solution": solution})

        puzzle = [
            [0, 4, 0, 0, 0, 0, 0, 0, 8],
            [0, 0, 0, 4, 0, 0, 6, 0, 3],
            [0, 0, 1, 0, 7, 9, 0, 2, 0],
            [7, 0, 0, 0, 0, 8, 0, 0, 2],
            [9, 0, 0, 0, 3, 0, 0, 0, 1],
            [6, 0, 0, 9, 0, 0, 0, 0, 7],
            [0, 7, 0, 3, 1, 0, 8, 0, 0],
            [1, 0, 9, 0, 0, 4, 0, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 1, 0],
        ]

        solution = [
            [2, 4, 7, 6, 5, 3, 1, 9, 8],
            [8, 9, 5, 4, 2, 1, 6, 7, 3],
            [3, 6, 1, 8, 7, 9, 4, 2, 5],
            [7, 5, 3, 1, 6, 8, 9, 4, 2],
            [9, 8, 4, 2, 3, 7, 5, 6, 1],
            [6, 1, 2, 9, 4, 5, 3, 8, 7],
            [4, 7, 6, 3, 1, 2, 8, 5, 9],
            [1, 2, 9, 5, 8, 4, 7, 3, 6],
            [5, 3, 8, 7, 9, 6, 2, 1, 4],
        ]
        self.boards.append({"puzzle": puzzle, "solution": solution})

    def test_example_incomplete(self):
        """Test case for the example given"""
        self.assertEqual(is_valid(self.boards[0]["puzzle"]), True)
        self.assertEqual(solve_sudoku(
            self.boards[0]["puzzle"]), self.boards[0]["solution"])

    def test_hard_puzzle(self):
        """Test case for the hard puzzle"""
        # Hard Puzzle 5,037,319,511 from https://www.websudoku.com/?level=3
        self.assertEqual(is_valid(self.boards[1]["puzzle"]), True)
        self.assertEqual(solve_sudoku(
            self.boards[1]["puzzle"]), self.boards[1]["solution"])

    def test_impossible_boards(self):
        """Test case for impossible boards"""
        board = [[1 for x in range(9)] for y in range(9)]
        self.assertEqual(is_valid(board), False)


if __name__ == "__main__":
    unittest.main()
