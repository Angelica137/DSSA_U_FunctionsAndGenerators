from scripts.exercise2 import check_sudoku


def test_check_sudoku_returns_true_if_list_has_int_only():
    assert check_sudoku([[1, 2, 3], [2, 3, 1], [3, 1, 2]]) == True


def test_check_sudoku_returns_false_if_list_empty():
    assert check_sudoku([]) == False
