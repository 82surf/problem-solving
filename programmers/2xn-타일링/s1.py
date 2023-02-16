def solution(n):
    if n < 3:
        return n
    a, b, c = 1, 2, 0
    cnt = 2
    while cnt < n:
        c = a + b
        a = b
        b = c
        cnt += 1
    return b % 1000000007