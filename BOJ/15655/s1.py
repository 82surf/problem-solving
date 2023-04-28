from itertools import combinations

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

for i in combinations(nums, M):
    print(*i)