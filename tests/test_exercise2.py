from scripts.exercise2 import check_sudoku


def test_check_sudoku_returns_true_if_list_has_int_only():
    assert check_sudoku([[1, 2, 3], [2, 3, 1], [3, 1, 2]]) == True


def test_check_sudoku_returns_false_if_list_has_non_int():
    assert check_sudoku([[1, 'b', 1],
                         ['b', 'c', 'a'],
                         ['c', 'a', 'b']]) == False


def test_check_sudoku_returns_true_if_elem_no_greter_length_list():
    assert check_sudoku([[1, 2, 3], [2, 3, 1], [3, 1, 2]]) == True


def test_sudoku_returns_false_if_elem_greater_len_list():
    assert check_sudoku([[1, 2, 3, 4, 5],
                         [2, 3, 1, 5, 6],
                         [4, 5, 2, 1, 3],
                         [3, 4, 5, 2, 1],
                         [5, 6, 4, 3, 2]]) == False
