from heapq import heappop, heappush
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
hq = []
for _ in range(N):
    x = int(input())
    if x == 0:
        print(heappop(hq)[1]) if hq else print(0)
    else:
        heappush(hq, (-x, x))