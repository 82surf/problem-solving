def solution(n):
    coin_5 = n // 5
    n -= coin_5 * 5
    coin_2 = n // 2
    n -= coin_2 * 2
    while n:
        coin_5 -= 1
        if coin_5 < 0:
            return -1
        n += 5
        extra_2 = n // 2
        coin_2 += extra_2
        n -= extra_2 * 2
    return coin_5 + coin_2


n = int(input())
print(solution(n))
