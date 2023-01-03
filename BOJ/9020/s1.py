# 시간초과

import sys
sys.stdin = open('input.txt')


def prime_list(n):
    sieve = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i + i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]


def gold_pair(p_list):
    for i in range(len(p_list) - 1, -1, -1):
        a = p_list[i]
        for j in range(len(p_list) - 1, i - 1, -1):
            b = p_list[j]
            if a + b == N:
                return (a, b)


for _ in range(int(input())):
    # N보다 작은 소수 구하기
    N = int(input())
    p_list = prime_list(N)

    # 2개를 더해 N이 되는 조합 구하기
    a, b = gold_pair(p_list)

    # 두 수의 차이가 더 적은 조합 출력하기
    print(a, b)