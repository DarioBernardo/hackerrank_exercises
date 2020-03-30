"""
In this version of the castle riddle. I can
only move to the end of the board or till an X.
In the next version I can stop at any time.
"""


def find_next_position_up(grid, curr_pos):
    next_pos = tuple(list(curr_pos))

    while next_pos[0] > 0 and grid[next_pos[0]-1][next_pos[1]] != 'X':
        next_pos = (next_pos[0] - 1, next_pos[1])

    if next_pos == curr_pos:
        return None
    else:
        return next_pos


def find_next_position_down(grid, curr_pos):
    next_pos = tuple(list(curr_pos))

    while next_pos[0] < len(grid)-1 and grid[next_pos[0]+1][next_pos[1]] != 'X':
        next_pos = (next_pos[0] + 1, next_pos[1])

    if next_pos == curr_pos:
        return None
    else:
        return next_pos


def find_next_position_left(grid, curr_pos):
    next_pos = tuple(list(curr_pos))

    while next_pos[1] > 0 and grid[next_pos[0]][next_pos[1]-1] != 'X':
        next_pos = (next_pos[0], next_pos[1] - 1)

    if next_pos == curr_pos:
        return None
    else:
        return next_pos


def find_next_position_right(grid, curr_pos):
    next_pos = tuple(list(curr_pos))

    while next_pos[1] < len(grid)-1 and grid[next_pos[0]][next_pos[1]+1] != 'X':
        next_pos = (next_pos[0], next_pos[1] + 1)

    if next_pos == curr_pos:
        return None
    else:
        return next_pos


# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    queue = [(startX, startY)]
    visited = {(startX, startY): 0}
    moves = [find_next_position_up, find_next_position_down, find_next_position_left, find_next_position_right]

    while len(queue) > 0:
        pos = queue.pop(0)
        steps_to_here = visited[pos]
        if pos[0] == goalX and pos[1] == goalY:
            return steps_to_here
        for move in moves:
            next_pos = move(grid, pos)
            if next_pos and next_pos not in visited:
                queue.append(next_pos)
                visited[next_pos] = steps_to_here + 1

    return -1


boards = [
    [
        ".X.",
        ".X.",
        "..."
    ],
    [
        ".X..XX...X",
        "X.........",
        ".X.......X",
        "..........",
        "........X.",
        ".X...XXX..",
        ".....X..XX",
        ".....X.X..",
        "..........",
        ".....X..XX"
    ],
    [
        ".X..XX...X",
        "X.........",
        ".........X",
        "..........",
        "........X.",
        ".X...XXX..",
        ".....X..XX",
        ".....X.X..",
        "..........",
        ".....X..XX"
    ]
]
start_and_end = [(0, 0, 0, 2), (9, 1, 1, 9), (9, 1, 0, 7)]
sols = [3, 3, 6]

for board, sol, coods in zip(boards, sols, start_and_end):
    mm = minimumMoves(board, coods[0], coods[1], coods[2], coods[3])
    print(mm)
    assert mm == sol

print("DONE!")
