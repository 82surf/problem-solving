import sys
sys.stdin = open('input.txt')


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


for _ in range(int(input())):
    N = int(input())
    a = N // 2
    while not (is_prime(N - a) and is_prime(a)):
        a -= 1
    print(a, N - a)