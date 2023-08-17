import sys
input = sys.stdin.readline

N = int(input())
dots = [0] * N
for i in range(N):
    x, y = map(int, input().split())
    dots[i] = (x, y)
dots.sort(key=lambda dot: (dot[0], dot[1]))

for dot in dots:
    print(*dot)