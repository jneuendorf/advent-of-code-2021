from functools import cache

data = """4,3,3,5,4,1,2,1,3,1,1,1,1,1,2,4,1,3,3,1,1,1,1,2,3,1,1,1,4,1,1,2,1,2,2,1,1,1,1,1,5,1,1,2,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,5,1,4,2,1,1,2,1,3,1,1,2,2,1,1,1,1,1,1,1,1,1,1,4,1,3,2,2,3,1,1,1,4,1,1,1,1,5,1,1,1,5,1,1,3,1,1,2,4,1,1,3,2,4,1,1,1,1,1,5,5,1,1,1,1,1,1,4,1,1,1,3,2,1,1,5,1,1,1,1,1,1,1,5,4,1,5,1,3,4,1,1,1,1,2,1,2,1,1,1,2,2,1,2,3,5,1,1,1,1,3,5,1,1,1,2,1,1,4,1,1,5,1,4,1,2,1,3,1,5,1,4,3,1,3,2,1,1,1,2,2,1,1,1,1,4,5,1,1,1,1,1,3,1,3,4,1,1,4,1,1,3,1,3,1,1,4,5,4,3,2,5,1,1,1,1,1,1,2,1,5,2,5,3,1,1,1,1,1,3,1,1,1,1,5,1,2,1,2,1,1,1,1,2,1,1,1,1,1,1,1,3,3,1,1,5,1,3,5,5,1,1,1,2,1,2,1,5,1,1,1,1,2,1,1,1,2,1"""
values = [int(n) for n in data.split(',')]


def calc_new1(start, value, days):
    if start >= days:
        return 0

    num_new = ((days - start + 1) - (value + 1)) // 7 + 1
    return num_new + calc_new1(start + value + 1, 8, days)


@cache
def calc_new(rem_days: int, value: int) -> int:
    if rem_days <= 0 or rem_days <= value:
        # print((rem_days, value, '->', 0))
        return 0

    children = (rem_days - value - 1) // 7 + 1
    # print('next rem days:', list(range(rem_days - value - 1, 0 - 1, -7)))
    grand_children = sum(calc_new(child_rem_days, 8) for child_rem_days in range(rem_days - value - 1, 0 - 1, -7))
    # print((rem_days, value, f'-> {children} + {grand_children}'))
    return children + grand_children


def p1(N: int = 80):
    return len(values) + sum(calc_new(N, value) for value in values)


def p2(N: int = 256):
    return p1(N)


print('6.1 ->', p1())
print('6.2 ->', p2())
