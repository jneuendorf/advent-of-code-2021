# import numpy as np
from functools import cache

data = """4,3,3,5,4,1,2,1,3,1,1,1,1,1,2,4,1,3,3,1,1,1,1,2,3,1,1,1,4,1,1,2,1,2,2,1,1,1,1,1,5,1,1,2,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,5,1,4,2,1,1,2,1,3,1,1,2,2,1,1,1,1,1,1,1,1,1,1,4,1,3,2,2,3,1,1,1,4,1,1,1,1,5,1,1,1,5,1,1,3,1,1,2,4,1,1,3,2,4,1,1,1,1,1,5,5,1,1,1,1,1,1,4,1,1,1,3,2,1,1,5,1,1,1,1,1,1,1,5,4,1,5,1,3,4,1,1,1,1,2,1,2,1,1,1,2,2,1,2,3,5,1,1,1,1,3,5,1,1,1,2,1,1,4,1,1,5,1,4,1,2,1,3,1,5,1,4,3,1,3,2,1,1,1,2,2,1,1,1,1,4,5,1,1,1,1,1,3,1,3,4,1,1,4,1,1,3,1,3,1,1,4,5,4,3,2,5,1,1,1,1,1,1,2,1,5,2,5,3,1,1,1,1,1,3,1,1,1,1,5,1,2,1,2,1,1,1,1,2,1,1,1,1,1,1,1,3,3,1,1,5,1,3,5,5,1,1,1,2,1,2,1,5,1,1,1,1,2,1,1,1,2,1"""
values = [int(n) for n in data.split(',')]


def f(start, value, days):
    return (
        num_new := ((days - start + 1) - (value + 1)) // 7 + 1,
        idx_first_new := start + value + 1,
        # idx_first_new := start + value,
    )


def calc_new1(start, value, days):
    if start >= days:
        return 0

    num_new = ((days - start + 1) - (value + 1)) // 7 + 1
    return num_new + calc_new1(start + value + 1, 8, days)


# cache: dict[tuple[int, int], int] = {}
args = set()


@cache
def calc_new(rem_days: int, value: int) -> int:
    print(rem_days, ',', value)
    if rem_days <= 0 or rem_days <= value:
        return 0

    # args = (rem_days, value)
    # if args not in cache:
    #     num_new = ((rem_days + 1) - (value + 1)) // 7 + 1
    #     cache[args] = num_new + calc_new(rem_days - value - 1, 8)
    # return cache[args]

    num_new = ((rem_days + 1) - (value + 1)) // 7 + 1
    args.add((rem_days, value, '->', num_new + calc_new(rem_days - value - 1, 8)))
    return num_new + calc_new(rem_days - value - 1, 8)


# def f_new(start, days):
#     return f(start, value=8, days=days)


def p1(N: int = 80):
    # data = "3,4,3,1,2"
    data = "3"
    values = [int(n) for n in data.split(',')]
    # state = np.array([int(n) for n in data.split(',')])
    # N = 80 + 1
    # for i in range(N):
    #     state -= 1
    #     num_new = np.sum(state == -1)
    #     if num_new > 0:
    #         state = np.array(list(state) + [8]*num_new)
    #     state[state == -1] = 6
    #     # print(i + 1, '->', state)
    # return state.size  # 387413
    # cols: set[tuple[int, int]] = {(1, value) for value in values}

    # cols = [(0, value) for value in values]
    # n = 0
    # # c = []
    # while cols:
    #     start, value = cols.pop(0)
    #     if start <= N:
    #         n += 1
    #         # new, idx = f(start, value, N)
    #         idx = start + value + 1
    #         # print(start, value, '->', new, idx)
    #         # c.append(
    #         #     (
    #         #         ([-1] * start) +
    #         #         list(range(value, -1, -1)) +
    #         #         list(range(6, -1, -1)) * N
    #         #     )[:N]
    #         # )
    #         for i in range(idx, N, 7):
    #             cols.append((i, 8))
    #     # else:
    #     #     print('drop', start, value)
    # # print(
    # #     np.array(
    # #         sorted(c, key=lambda l: len([x for x in l if x >= 0]), reverse=True)
    # #     ).T
    # # )
    # return n

    # return sum(calc_new1(0, value, N) for value in values)
    return len(values) + sum(calc_new(N, value) for value in values)


def p2():

    N = 256 + 1
    # state = np.array([int(n) for n in data.split(',')])
    # for i in range(N):
    #     state -= 1
    #     num_new = np.sum(state == -1)
    #     if num_new > 0:
    #         state = np.array(list(state) + [8] * num_new)
    #     state[state == -1] = 6
    #     # print(i + 1, '->', state)
    # return state.size
    cols = [(0, value) for value in values]
    n = 0
    while cols:
        start, value = cols.pop(0)
        n += 1
        idx = start + value + 1
        for i in range(idx, N, 7):
            cols.append((i, 8))

    return n


# p1_test()
for i in range(19):
    print('after', i, '->', p1(i))
# print('6.1 ->', p1())
# print(args)
# print('6.2 ->', p2())
