

def answer(t, n):
    state = [0] * (n + 1)
    # mark leftmost square.
    state[1] = 1
    for cur_t in range(t):
        begin = max(1, n - t + cur_t)
        new_state = [0] * (n + 1)
        # copy [n]
        new_state[n] = state[n]
        # deal with [begin, n - 1].
        for i in range(begin, n):
            new_state[i - 1] += state[i]
            new_state[i] += state[i]
            new_state[i + 1] += state[i]
        state = new_state
    return state[n] % 123454321
