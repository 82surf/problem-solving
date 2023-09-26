from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def solution():
    def d(n):
        n *= 2
        if n > 9999:
            n %= 10000
        return n

    def s(n):
        n -= 1
        if n < 0:
            n = 9999
        return n

    def l(n):
        digit_4 = n // 1000
        n -= digit_4 * 1000
        n *= 10
        n += digit_4
        return n

    def r(n):
        digit_1 = n % 10
        n //= 10
        n += digit_1 * (10 ** 3)
        return n

    def BFS(start, target):
        q = deque([(start, '')])
        visited = [0] * 10001
        visited[start] = 1
        funcs = { 'D': d, 'S': s, 'L': l, 'R': r }
        while q:
            num, oprs = q.popleft()
            if num == target:
                return oprs

            for opr, func in funcs.items():
                next_n = func(num)
                if not visited[next_n]:
                    q.append((next_n, oprs + opr))
                    visited[next_n] = 1

    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        print(BFS(a, b))


solution()