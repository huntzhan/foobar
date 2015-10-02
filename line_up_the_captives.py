from math import factorial


def install_cache(func):
    cache = {}

    def _wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return _wrapper


@install_cache
def choose(n, k):
    if k < 0 or k > n:
        return 0
    # normal case.
    nominator = 1
    denominator = 1
    count = 1
    while count <= k:
        nominator *= n
        denominator *= count
        count += 1
        n -= 1
    return nominator // denominator


def prepare_matrix(n):
    # row: total number of rabbits.
    # col: number of rabbits to be seen.
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    # fill diagonal with 1.
    for i in range(1, n + 1):
        dp[i][i] = 1
    # special case: (0, 0)
    dp[0][0] = 1

    # dp!
    for i in range(2, n + 1):      # size of group.
        for j in range(1, i):      # size to be seen.
            for k in range(0, i):  # size of subgroup.
                dp[i][j] += (choose(i - 1, k) * dp[k][j - 1]
                             * factorial(i - 1 - k))
    return dp


def answer(x, y, n):
    dp = prepare_matrix(n)
    # the tallest rabbit split a group into two parts.
    west_group_size = x - 1
    east_group_size = y - 1
    pool_size = n - 1 - west_group_size - east_group_size
    if pool_size < 0:
        return 0
    # counting.
    count = 0
    for addend in range(pool_size + 1):
        west_count = dp[west_group_size + addend][west_group_size]
        east_count = dp[east_group_size + pool_size - addend][east_group_size]
        # accumulate the result.
        kinds = choose(n - 1, west_group_size + addend)
        count += kinds * west_count * east_count
    return count
