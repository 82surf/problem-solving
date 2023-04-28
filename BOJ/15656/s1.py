from itertools import product

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
for i in product(nums, repeat=M):
    print(*i)