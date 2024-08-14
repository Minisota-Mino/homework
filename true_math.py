from math import inf


def divide_2(first, second):
    if second > 0:
        print(first / second)
    elif second == 0:
        print(inf)
    return inf
