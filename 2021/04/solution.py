def get_input(filename):
    called = None
    boards = []
    idx = -1
    with open(filename, 'r') as f:
        board_idx = 0
        for line in [l.strip() for l in f.readlines()]:
            if ',' in line and called == None:
                called = [int(x) for x in line.split(',')]
            elif line == '':
                boards.append([[[0 for _ in range(0, 5)] for _ in range(0, 5)],
                               [[0 for _ in range(0, 5)] for _ in range(0, 5)]])
                board_idx = 0
                idx += 1
            else:
                nums = [int(x) for x in line.split()]
                boards[idx][0][board_idx] = nums
                board_idx += 1
    return called, boards

def first():
    called, boards = get_input('data.txt')
    iteration = 0
    for bingo_ball in called:
        for board_num, board_set in enumerate(boards):
            for row, vals in enumerate(board_set[0]):
                for col, val in enumerate(vals):
                    iteration += 1
                    if bingo_ball == boards[board_num][0][row][col]:
                        boards[board_num][1][row][col] = 1
                        if check_for_solved(boards[board_num][1]):
                            return get_unmarked(boards[board_num]) * val
    raise ValueError('did not find a solution!')


def check_for_solved(board):
    for row_num in range(0, 5):
        if sum(board[row_num]) == 5:
            return True
    for col_num in range(0, 5):
        if sum([v[col_num] for v in board]) == 5:
            return True
    return False


def get_unmarked(boards):
    total = 0
    for row_num in range(0, 5):
        for col_num in range(0, 5):
            if boards[1][row_num][col_num] == 0:
                total += boards[0][row_num][col_num]
    return total

def second():
    called, boards = get_input('data.txt')
    iteration = 0
    remaining = set([x for x in range(0, len(boards))])
    for bingo_ball in called:
        for board_num, board_set in enumerate(boards):
            for row, vals in enumerate(board_set[0]):
                for col, val in enumerate(vals):
                    iteration += 1
                    if bingo_ball == boards[board_num][0][row][col]:
                        boards[board_num][1][row][col] = 1
                        if check_for_solved(boards[board_num][1]):
                            remaining.discard(board_num)
                        if len(remaining) == 0:
                            return get_unmarked(boards[board_num]) * val
    raise ValueError('did not find a solution!')

print(first())
print(second())
