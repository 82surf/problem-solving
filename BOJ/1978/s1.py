# import sys
# sys.stdin = open('input.txt')


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True

N = input()
nums = list(map(int, input().split()))
cnt = 0
for n in nums:
    if is_prime(n):
        cnt += 1
print(cnt)
