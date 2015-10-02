from __future__ import division


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
    if k == n or k == 0:
        return 1

    nominator = 1
    denominator = 1
    count = 1
    while count <= k:
        nominator *= n
        denominator *= count
        count += 1
        n -= 1

    return nominator // denominator


@install_cache
def count(n, k):
    # promise: n - 1 <= k <= choose(n, 2)
    if k == n - 1:
        return int(n ** (n - 2))
    if k == choose(n, 2):
        return 1

    combinations = choose(choose(n, 2), k)
    if k > choose(n - 1, 2):
        # cannot be split.
        return combinations

    # remove forests.
    # create a split: connected component with i vertices, and others.
    for i in range(1, n):
        kinds = choose(n - 1, i - 1)
        max_edge_size = min(choose(i, 2), k)
        for edge_size in range(i - 1, max_edge_size + 1):
            combinations -= (kinds
                             * count(i, edge_size)
                             * choose(choose(n - i, 2), k - edge_size))
    return combinations


def answer(n, k):
    return str(count(n, k))
