"""
CSCA08: Winter 2024 -- Assignment 2: Wacky Wonderland

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.
"""

# deepcopy() is used to make sure we can easily clone arrays.
# An example of how it's used is given on the assignment handout.
from copy import deepcopy

# The constants below are provided as test data and can be
# modified and used inside your docstrings to test your functions.

TEST_ACC_NUM_A = [1, 9, 4, 5, 5, 7, 2]

SAMPLE_MATRIX_A = [
    [3, 4, 5],
    [8, 8, 8],
    [1, 0, 5],
    [1, 8, 7]
]

SAMPLE_MATRIX_A_T = [
    [3, 8, 1, 1],
    [4, 8, 0, 8],
    [5, 8, 5, 7],
]

SAMPLE_MATRIX_B = [
    [3, 4, 5, 2, 9, 1, 5, 3, 2, 8],
    [8, 8, 8, 9, 2, 7, 8, 7, 3, 5],
    [1, 0, 5, 2, 4, 9, 4, 0, 3, 8],
    [1, 8, 7, 5, 6, 2, 4, 9, 7, 1],
    [6, 3, 3, 8, 7, 3, 3, 2, 2, 9],
    [0, 2, 4, 5, 1, 9, 4, 2, 8, 5],
    [9, 6, 7, 0, 2, 4, 1, 0, 2, 1],
    [1, 5, 9, 0, 2, 4, 2, 2, 4, 6],
    [5, 5, 4, 9, 3, 1, 2, 3, 4, 0],
    [2, 6, 7, 9, 9, 5, 3, 8, 2, 2]
]

### (non-square matrix)
SAMPLE_MATRIX_C = [
    [3, 4, 5, 2, 9, 1, 5, 3, 2, 8, 1],
    [8, 8, 8, 9, 2, 7, 8, 7, 3, 5, 1],
    [1, 0, 5, 2, 4, 9, 4, 0, 3, 8, 1],
    [1, 8, 7, 5, 6, 2, 4, 9, 7, 1, 1],
    [6, 3, 3, 8, 7, 3, 3, 2, 2, 9, 1],
    [0, 2, 4, 5, 1, 9, 4, 2, 8, 5, 1],
    [9, 6, 7, 0, 2, 4, 1, 0, 2, 1, 1],
    [1, 5, 9, 0, 2, 4, 2, 2, 4, 6, 1],
    [5, 5, 4, 9, 3, 1, 2, 3, 4, 0, 1],
    [2, 6, 7, 9, 9, 5, 3, 8, 2, 2, 1]
]

#############################################################
### PART 1 : Account Numbers
#############################################################

def sum_of_digits(number: int) -> int:
    '''
    Given a non-negative integer 'number', return the sum of all its digits.

    Preconditions: number >= 0

    >>> sum_of_digits(1234)
    10
    >>> sum_of_digits(8888)
    32
    '''

    return sum(int(x) for x in str(number))


def is_valid_account(num_array: list[int]) -> bool:
    '''
    Given the account number in the format of an integer list 'num_array',
    return whether the account number is valid based on Wacky's Algorithm.

    Preconditions: len(num_array) >= 3

    >>> is_valid_account([1, 9, 4, 5, 5, 7, 2])
    False
    >>> is_valid_account([3, 7, 6, 4, 7, 9, 0, 6])
    True
    '''

    my_array = deepcopy(num_array)
    for i in range(len(num_array) - 3, -1, -1):
        my_array[i] = sum_of_digits(my_array[i] * my_array[-2])
    return sum(my_array) % 10 == num_array[-1]


#############################################################
### PART 2 : Memory Trail
#############################################################

def memory_median(num_array: list[int]) -> float:
    '''
    Given a list of integers 'num_array', return the median of the list.
    Note that if len(num_array) == 2, the median is the average of the
    two middle numbers.

    Preconditions: len(num_array) >= 1

    >>> memory_median([5, 7, 9, 8, 2, 1, 6, 3])
    5.5
    >>> memory_median([3, 1, 4])
    3
    '''

    sorted_array = sorted(num_array)
    mid = len(sorted_array) // 2
    if len(sorted_array) % 2 == 0:
        return (sorted_array[mid-1] + sorted_array[mid]) / 2
    return sorted_array[mid]


def memory_sequence(num_array: list[int]) -> list[int]:
    '''
    Given a list of integers 'num_array', return a modified list based on
    'num_array', where only the first occurence of an integer is kept.

    Preconditions: len(num_array) >= 1

    >>> memory_sequence([1, 1, 3, 2, 2, 4, 5, 2])
    [1, 3, 2, 4, 5]
    >>> memory_sequence([1, 1, 1, 1, 1])
    [1]
    '''

    flag = {}
    ret = []
    for item in num_array:
        if item not in flag:
            flag[item] = True
            ret.append(item)
    return ret


def memory_count(num_array: list[int], recall_array: list[int]) -> list[int]:
    '''
    Given two lists of integers 'num_array' and 'recall_array', return a new
    list of array based on 'recall_array', where each item represents the number
    of times the item in 'recall_array' appears in 'num_array'.

    Preconditions: len(num_array) >= 1
                   len(recall_array) >= 1

    >>> memory_count([1, 1, 3, 2, 2, 4, 5, 2], [1, 5, 7, 2])
    [2, 1, 0, 3]
    >>> memory_count([1, 1, 1, 1, 1], [0, 2, 3])
    [0, 0, 0]
    '''

    cnt = {}
    for item in num_array:
        cnt[item] = 1 if item not in cnt else cnt[item] + 1
    return [0 if x not in cnt else cnt[x] for x in recall_array]


#############################################################
### PART 3 : Numbers Search
#############################################################

def in_matrix(row: int, col: int, max_rows: int, max_cols: int) -> bool:
    '''
    Return True if and only if a given row and column index 'row'
    'col' are inside a matrix with 'max_rows' number of rows and
    'max_cols' number of columns.

    Preconditions: max_rows >= 0
                   max_cols >= 0

    >>> in_matrix(3, 4, 6, 6)
    True
    >>> in_matrix(10, 10, 5, 5)
    False
    '''

    return row in range(0, max_rows) and col in range(0, max_cols)


def swap_around(matrix: list[list[int]]) -> list[list[int]]:
    '''
    Return a swapped around matrix based on the given 'matrix'. Specifically,
    a new matrix where each column (left-to-right) in new matrix
    represents each row (top-to-down) in old matrix 'matrix'. For each
    column in new matrix, the numbers from top to down are the numbers
    from left to right in the corresponding row of the old matrix.

    Preconditions: len(matrix) == N
                   len(matrix[i]) == M, 0 <= i < N

    >>> swap_around(SAMPLE_MATRIX_A) == SAMPLE_MATRIX_A_T
    True
    >>> swap_around([[2, 3, 4], [6, 7, 8]]) == [[2, 6], [3, 7], [4, 8]]
    True
    >>> swap_around([[1]]) == [[1]]
    True
    '''

    rows = len(matrix)
    cols = len(matrix[0])

    # init ret matrix
    ret = []
    for i in range(cols):
        row = []
        for j in range(rows):
            row.append(0)
        ret.append(row)

    for i in range(rows):
        for j in range(cols):
            ret[j][i] = matrix[i][j]
    return ret


def search_list(num_list: list[int], series: list[int]) -> int:
    '''
    Return the index of the first occurence of 'series' or reversed
    'series' in a list of integers 'num_list'. If no matches are found,
    return -1.

    Preconditions: len(num_list) >= 1
                   len(series) >= 1

    >>> SAMPLE_LIST = [3, 4, 5, 8, 8, 8, 1, 0, 5]
    >>> search_list(SAMPLE_LIST, [5, 8, 8])
    2
    >>> search_list(SAMPLE_LIST, [8, 8, 5])
    2
    >>> search_list(SAMPLE_LIST, [1, 1, 1])
    -1
    >>> search_list([3, 4, 5, 3, 4, 5], [5, 4, 3])
    0
    '''

    if len(num_list) < len(series):
        return -1

    min_idx = len(num_list) + 1
    for i in range(len(num_list) - len(series) + 1):
        found = True
        for j in range(len(series)):
            if series[j] != num_list[i + j]:
                found = False
                break
        if found:
            min_idx = min(min_idx, i)
        found = True
        for j in range(len(series)):
            if series[len(series) - j - 1] != num_list[i + j]:
                found = False
                break
        if found:
            min_idx = min(min_idx, i)
    return min_idx if min_idx != len(num_list) + 1 else -1

def search_rows(matrix: list[list[int]], series: list[int]) -> bool:
    '''
    Return whether the list of integers 'seires' can be found in
    original or revsered order in any row of 'matrix'.

    Preconditions: len(matrix) == N
                   len(matrix[i]) == M, 0 <= i < N
                   len(series) >= 1

    >>> search_rows(SAMPLE_MATRIX_B, [8, 7, 3, 3])
    True
    >>> search_rows(SAMPLE_MATRIX_B, [4, 3, 2, 1])
    True
    >>> search_rows(SAMPLE_MATRIX_B, [1, 1, 1])
    False
    '''

    for row in matrix:
        if search_list(row, series) != -1:
            return True
    return False


def search_columns(matrix: list[list[int]], series: list[int]) -> bool:
    '''
    Return whether the list of integers 'seires' can be found in
    original or revsered order in any column of 'matrix'.

    Preconditions: len(matrix) == N
                   len(matrix[i]) == M, 0 <= i < N
                   len(series) >= 1

    >>> search_columns(SAMPLE_MATRIX_B, [3, 9, 4, 4])
    True
    >>> search_columns(SAMPLE_MATRIX_B, [7, 4, 3, 7])
    True
    >>> search_columns(SAMPLE_MATRIX_B, [1, 2, 3, 4])
    False
    >>> search_columns(SAMPLE_MATRIX_C, [1, 1, 1, 1])
    True
    '''

    swapped_matrix = swap_around(matrix)
    return search_rows(swapped_matrix, series)


def search_diagonals(matrix: list[list[int]], series: list[int]) -> bool:
    '''
    Return whether the list of integers 'seires' can be found in
    original or revsered order in any diagonals of 'matrix'.

    Preconditions: len(matrix) == N
                   len(matrix[i]) == M, 0 <= i < N
                   len(series) >= 1

    >>> search_diagonals(SAMPLE_MATRIX_B, [3, 1, 0, 9, 5])
    True
    >>> search_diagonals(SAMPLE_MATRIX_B, [9, 9, 6, 0])
    True
    >>> search_diagonals(SAMPLE_MATRIX_B, [1, 2, 3, 4])
    False
    >>> search_diagonals(SAMPLE_MATRIX_C, [1, 5, 3, 9, 3])
    True
    >>> search_diagonals(SAMPLE_MATRIX_C, [5, 1, 3, 9, 3])
    False
    '''

    rows = len(matrix)
    cols = len(matrix[0])
    lsts = []

    # for i in range(rows):
    #     print(matrix[i])
    # print(" === ")

    # top-left -> bottom-right
    # bottom-left part
    for i in range(rows):
        lst = []
        for j in range(min(rows - i, cols - i)):
            lst.append(matrix[i + j][j])
        lsts.append(lst)
        # print(l)
        # if search_list(lst, series) != -1:
            # return "found in tl-br (bl)"
            # return True
    # top-right part
    for i in range(1, cols):
        lst = []
        for j in range(max(rows - i, cols - i)):
            lst.append(matrix[j][i + j])
        lsts.append(lst)
        # print(l)
        # if search_list(lst, series) != -1:
            # return "found in tl-br (tr)"
            # return True

    # bottom-left -> top-right
    # top-left
    for i in range(rows):
        lst = []
        for j in range(i + 1):
            lst.append(matrix[i - j][j])
        lsts.append(lst)
        # print(l)
        # if search_list(lst, series) != -1:
            # return "found in bl-tr (tl)"
            # return True
    # bottom-right
    for i in range(cols - 1, 0, -1):
        lst = []
        for j in range(cols - i):
            lst.append(matrix[rows - j - 1][i + j])
        lsts.append(lst)
        # print(l)
        # if search_list(lst, series) != -1:
            # return "found in bl-tr (br)"
            # return True

    return any(search_list(x, series) != -1 for x in lsts)

def validate_coordinates(matrix: list[list[int]], row_idx: int,
                         col_idx: int, series: list[int]) -> bool:
    '''
    Return whether the list of numbers 'series' can be found at and overlap
    the given ['row_idx', 'cod_idx'] coordinates either via row, column or
    diagonal.

    Preconditions: len(matrix) == N
                   len(matrix[i]) == M, 0 <= i < N
                   0 <= row_idx < N
                   0 <= col_idx < M
                   len(series) >= 1

    >>> validate_coordinates(SAMPLE_MATRIX_B, 4, 3, [4, 1, 8, 7, 0, 8])
    True
    >>> validate_coordinates(SAMPLE_MATRIX_B, 5, 7, [7, 0, 9, 2, 2])
    True
    >>> validate_coordinates(SAMPLE_MATRIX_B, 9, 0, [7, 9, 9, 5])
    False
    >>> validate_coordinates(SAMPLE_MATRIX_C, 0, 10, [1, 5, 3, 9, 3])
    True
    >>> validate_coordinates(SAMPLE_MATRIX_C, 1, 9, [3, 9, 3, 5, 1])
    True
    >>> validate_coordinates(SAMPLE_MATRIX_C, 0, 10, [1, 1, 1, 1, 1])
    True
    '''

    slen = len(series)
    rows = len(matrix)
    cols = len(matrix[0])

    row = matrix[row_idx][max(0, col_idx - slen + 1) : \
                          min(cols, col_idx + slen)]
    if search_list(row, series) != -1:
        return True

    col = []
    for i in range(max(0, row_idx - slen + 1), min(rows, row_idx + slen)):
        col += [matrix[i][col_idx]]
    if search_list(col, series) != -1:
        return True

    diagonal_tl_br = []
    for (i, j) in zip(range(row_idx - slen + 1, row_idx + slen), \
            range(col_idx - slen + 1, col_idx + slen)):
        if not in_matrix(i, j, rows, cols):
            continue
        diagonal_tl_br += [matrix[i][j]]
    if search_list(diagonal_tl_br, series) != -1:
        return True

    diagonal_tr_bl = []
    for (i, j) in zip(range(row_idx + slen - 1, row_idx - slen, -1), \
            range(col_idx - slen + 1, col_idx + slen)):
        if not in_matrix(i, j, rows, cols):
            continue
        diagonal_tr_bl += [matrix[i][j]]
    if search_list(diagonal_tr_bl, series) != -1:
        return True

    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # validate_coordinates(SAMPLE_MATRIX_C, 0, 10, [1, 5, 3, 9, 3])
    # search_diagonals(SAMPLE_MATRIX_B, [1, 2, 3, 4])
    # search_diagonals(SAMPLE_MATRIX_B, [3,1,0,9,5])
    # for row in SAMPLE_MATRIX_B:
    #     print(row)
    # print("===")
    # swapped = swap_around(SAMPLE_MATRIX_B)
    # for row in swapped:
    #     print(row)
