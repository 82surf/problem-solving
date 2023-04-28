from itertools import product

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
results = set()

for i in product(nums, repeat=M):
    if i not in results:
        results.add(i)
        print(*i)