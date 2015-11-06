def answer(L, k):
    max_sum = 0
    n = len(L)

    pre_sum = [0] * n
    size = [0] * n

    pre_sum[0] = L[0]
    size[0] = 1

    for end in range(1, n):
        pre_sum[end] = L[end]
        if pre_sum[end - 1] > 0:
            if size[end - 1] < k:
                pre_sum[end] += pre_sum[end - 1]
                size[end] = size[end - 1] + 1
            elif size[end - 1] == k:
                tmp_max_sum = -1
                tmp_max_size = -1
                tmp_sum = pre_sum[end - 1]

                for begin in range(end - k, end):
                    tmp_sum -= L[begin]
                    if tmp_sum > tmp_max_sum:
                        tmp_max_sum = tmp_sum
                        tmp_max_size = end - 1 - begin

                if tmp_max_sum < 0:
                    tmp_max_sum = 0
                    tmp_max_size = 0
                pre_sum[end] += tmp_max_sum
                size[end] = tmp_max_size + 1

        max_sum = max(max_sum, pre_sum[end])

    return max_sum
