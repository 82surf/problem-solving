from itertools import combinations_with_replacement

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
results = set()

for i in combinations_with_replacement(nums, M):
    if i not in results:
        results.add(i)
        print(*i)