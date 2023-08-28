from heapq import heappop, heappush
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

hq = []
hq_check = {}
for num in nums:
    if num not in hq_check:
        hq_check[num] = 1
        heappush(hq, num)

result = {}
cnt = 0
while hq:
    result[heappop(hq)] = cnt
    cnt += 1

for num in nums:
    print(result[num], end=' ')