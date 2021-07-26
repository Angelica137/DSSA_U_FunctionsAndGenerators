from scripts.exercise2 import check_sudoku


def test_check_sudoku_returns_true_if_list_given():
    assert check_sudoku([[1, 2, 3], [2, 3, 1], [3, 1, 2]]) == True
