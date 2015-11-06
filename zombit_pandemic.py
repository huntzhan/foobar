
from math import factorial
from operator import mul
from fractions import gcd

# used for memoizing the total number of single-tree connected forests
mem_single = {}

# used for memoizing binomial coefficient calculations
mem_choose = {}


def S(n):
    """
    Returns the number of pseudoforests with exactly one connected component
    involving all the nodes, ie. all nodes connected by a single tree.
    'A000435' requires float division, so I'm using 'A001864 / n' instead.
    """
    if n not in mem_single:
        values = (choose(n, k) * (n - k) ** (n - k) * k ** k
                  for k in range(1, n))
        mem_single[n] = sum(values) / n

    return mem_single[n]


def binomial(n, k):
    """
    Calculates the binomial coefficient for n, k.
    This is equivalent to 'n choose k'.

    http://stackoverflow.com/a/3025547/374865
    """
    if k > n:
        return 0

    elif k == 0 or n == k:
        return 1

    elif k == 1 or k == n - 1:
        return n

    else:
        if k > n >> 1:
            k = n - k

        a = 1
        b = 1
        for t in range(1, k + 1):
            a *= n
            b *= t
            n -= 1

        return a // b


def choose(n, k):
    """
    Memoized binomial coefficient to count combinations
    """
    if (n, k) not in mem_choose:
        mem_choose[(n, k)] = binomial(n, k)

    return mem_choose[(n, k)]


def C(n, partition):
    """
    Returns the number of ways n labelled items can be split
    according to a given partition
    """
    num = 1
    s = 0

    # counts the number of ways of splitting n labelled nodes into connected
    # components of the sizes given by the partition
    for i in range(len(partition)):
        num *= choose(n - s, partition[i])
        s += partition[i]

    # multiplicities of each member of the partition
    m = [partition.count(p) for p in set(partition)]

    # multiplication reduction of the factorial of each multiplicity
    den = reduce(mul, map(factorial, m))

    return num / den


def partitions(n):
    """
    Generates all integer partitions of n
    """
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while x << 1 <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            p = a[:k + 2]

            # ignore all trees of one node
            if 1 not in p:
                yield p

            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        p = a[:k + 1]

        # ignore all trees of one node
        if 1 not in p:
            yield p


def numerator(n):
    """
    Calculates the numerator of the answer
    """
    return sum(max(p) * C(n, p) * reduce(mul, map(S, p)) for p in partitions(n))


def answer(n):

    num = numerator(n)

    # denominator is the total number of forests for N
    den = (n - 1) ** n

    # reduce the fraction using the greatest common divisor
    div = gcd(num, den)

    return "%d/%d" % (num / div, den / div)
