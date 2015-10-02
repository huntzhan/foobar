

# def answer(numbers):
#     # states[i]: current count.
#     states = [0] * len(numbers)
#     index = 0
#     count = 0
#     while states[index] == 0:
#         states[index] = count
#         count += 1
#         index = numbers[index]
#     return count - states[index]


def answer(numbers):
    count = 0
    exists = set()
    for word in numbers:
        reversed_word = word[::-1]
        if word not in exists and reversed_word not in exists:
            count += 1
            exists.add(word)
    return count
