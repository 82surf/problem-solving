from heapq import heappush, heappop
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            abs_n, n = heappop(arr)
            print(n)
    else:
        heappush(arr, (abs(x), x))
