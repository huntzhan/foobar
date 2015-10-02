from math import sqrt


def answer(n):
    dp = [0] * (n + 1)
    for k in range(1, int(sqrt(n)) + 1):
        square_of_k = k ** 2
        dp[square_of_k] = 1
        for i in range(square_of_k + 1, min((k + 1) ** 2, n + 1)):
            dp[i] = dp[i - square_of_k] + 1
    return dp[n]
