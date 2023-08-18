import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
dots = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda dot: (dot[1], dot[0]))
for dot in dots:
    print(*dot)
