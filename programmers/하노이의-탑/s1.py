def cross(a, b, arrs):
    for arr in arrs:
        for i, n in enumerate(arr):
            if n == a:
                arr[i] = b
            elif n == b:
                arr[i] = a
    return arrs


def hanoi(n):
    if n == 1:
        return [[1, 3]]
    part1 = cross(2, 3, hanoi(n - 1))
    part2 = cross(1, 2, hanoi(n - 1))

    return part1 + [[1, 3]] + part2


def solution(n):
    return hanoi(n)