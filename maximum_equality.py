
def answer(x):
    base = len(x)
    number = sum(x)
    offset = number % base
    if offset == 0:
        return base
    elif offset < base - offset:
        return base - 1
    else:
        max_num = (number / base) + 1
        right_merged = number - max_num * offset
        return offset + right_merged / max_num
