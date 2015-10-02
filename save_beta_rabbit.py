
# DP: wrong way to do.
# def answer(food, grid):
#     COUNT_MAX = 999
#     N = len(grid)
#     dp = [[0] * N] * N
#     dp[0][0] = food
#
#     for row in range(N):
#         for col in range(N):
#             # skip top-left room.
#             if row == 0 and col == 0:
#                 continue
#
#             # prepare data.
#             left_min = COUNT_MAX
#             top_min = COUNT_MAX
#             if col > 0:
#                 left_min = dp[row][col - 1]
#             if row > 0:
#                 top_min = dp[row - 1][col]
#
#             # update.
#             with_left = -1
#             with_top = -1
#             if left_min != COUNT_MAX:
#                 with_left = left_min - grid[row][col]
#             if top_min != COUNT_MAX:
#                 with_top = top_min - grid[row][col]
#
#             if with_left >= 0 and with_top >= 0:
#                 dp[row][col] = min(with_left, with_top)
#             else:
#                 dp[row][col] = max(with_left, with_top)
#     return dp[N - 1][N - 1]


# dfs: ETL
# def dfs(food, grid, row, col):
#     upper_bound = len(grid) - 1
#     # exit.
#     if row == upper_bound and col == upper_bound:
#         return food - grid[row][col]
#     # invalid case.
#     if row < 0 or row > upper_bound:
#         return -1
#     if col < 0 or col > upper_bound:
#         return -1
#     if food < 0:
#         return -1
#
#     comsumed_food = food - grid[row][col]
#     down = dfs(comsumed_food, grid, row + 1, col)
#     right = dfs(comsumed_food, grid, row, col + 1)
#     if down >= 0 and right >= 0:
#         return min(down, right)
#     else:
#         return max(down, right)
#
# def answer(food, grid):
#     return dfs(food, grid, 0, 0)


def generate_boundary(grid):
    N = len(grid)
    # upper_bound[i][j]: maximum cost from (i, j) to (N - 1, N - 1)
    upper_bound = [[0 for c in range(N)] for r in range(N)]
    # lower_bound[i][j]: minimum cost from (i, j) to (N - 1, N - 1)
    lower_bound = [[0 for c in range(N)] for r in range(N)]
    # init.
    upper_bound[N - 1][N - 1] = grid[N - 1][N - 1]
    lower_bound[N - 1][N - 1] = grid[N - 1][N - 1]

    for row in reversed(range(N)):
        for col in reversed(range(N)):
            if row == N - 1 and col == N - 1:
                continue

            down_upper = None if row == N - 1 else upper_bound[row + 1][col]
            right_upper = None if col == N - 1 else upper_bound[row][col + 1]

            down_lower = None if row == N - 1 else lower_bound[row + 1][col]
            right_lower = None if col == N - 1 else lower_bound[row][col + 1]

            not_none = lambda x: x is not None
            upper_bound[row][col] = max(
                filter(not_none, (down_upper, right_upper)),
            )
            lower_bound[row][col] = min(
                filter(not_none, (down_lower, right_lower)),
            )

            upper_bound[row][col] += grid[row][col]
            lower_bound[row][col] += grid[row][col]

    return upper_bound, lower_bound


def search(row, col, food, grid, upper_bound, lower_bound):
    N = len(grid)
    # boundary check.
    if row < 0 or row >= N:
        return -1
    if col < 0 or col >= N:
        return -1

    # check lower_bound.
    if food < lower_bound[row][col]:
        # must die anyway.
        return -1
    if food == lower_bound[row][col]:
        # just enough food.
        return 0
    # check upper_bound.
    if food >= upper_bound[row][col]:
        # optimal solution.
        return food - upper_bound[row][col]

    # feed the zoombie.
    food -= grid[row][col]
    # stop recursion.
    if row == N - 1 and col == N - 1:
        return max(food, -1)

    # food within range (upper_bound, lower_bound).
    # so, keep searching.
    down = search(row + 1, col, food, grid, upper_bound, lower_bound)
    right = search(row, col + 1, food, grid, upper_bound, lower_bound)
    if down >= 0 and right >= 0:
        return min(down, right)
    else:
        return max(down, right)


def answer(food, grid):
    upper_bound, lower_bound = generate_boundary(grid)
    return search(0, 0, food, grid, upper_bound, lower_bound)
