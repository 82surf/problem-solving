from itertools import combinations

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
results = set()

for i in combinations(nums, M):
    if i not in results:
        results.add(i)
        print(*i)