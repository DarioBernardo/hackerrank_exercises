input_grids = [
    [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]],
    [[0, 0, 1, 1], [0, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]],
    [[1, 0, 1, 1, 0], [1, 1, 0, 0, 1], [0, 1, 1, 1, 0], [0, 0, 0, 0, 1], [1, 1, 1, 0, 0]]
]

solutions = [5, 8, 10]


def get_children(g, i, j) -> list:
    children = []
    x_len = len(g)
    y_len = len(g[0])
    for row_displacement in range(-1, 2):
        for col_displacement in range(-1, 2):
            if not (row_displacement == 0 and col_displacement == 0):
                new_row_coord = i + row_displacement
                new_col_coord = j + col_displacement
                if x_len > new_row_coord >= 0 and y_len > new_col_coord >= 0:
                    if g[new_row_coord][new_col_coord] == 1:
                        children.append((new_row_coord, new_col_coord))

    return children


def dfs(g, visited, i, j) -> int:
    children = get_children(g, i, j)
    current_covered_area = 1
    visited.add((i, j))
    for child in children:
        if child not in visited:
            current_covered_area += dfs(g, visited, child[0], child[1])

    return current_covered_area


# Complete the maxRegion function below.
def maxRegion(grid):
    x_len = len(grid)
    y_len = len(grid[0])
    visited_nodes = set()
    max_covered_area = 0
    for i in range(0, x_len):
        for j in range(0, y_len):
            if grid[i][j] == 1:
                if (i, j) not in visited_nodes:
                    covered_area = dfs(grid, visited_nodes, i, j)
                    max_covered_area = max(max_covered_area, covered_area)

    return max_covered_area


for grid, sol in zip(input_grids, solutions):
    my_sol = maxRegion(grid)
    print(my_sol)
    assert my_sol == sol

print("DONE!")
