from heapq import heappop, heappush
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
hq = []
for _ in range(N):
    num = int(input())
    if num != 0:
        heappush(hq, num)
    elif len(hq) == 0:
        print(0)
    else:
        print(heappop(hq))
