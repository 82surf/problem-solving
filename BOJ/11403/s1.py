from math import inf
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = inf

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(N):
    for j in range(N):
        if graph[i][j] == inf:
            graph[i][j] = 0
        elif graph[i][j]:
            graph[i][j] = 1

for g in graph:
    print(*g)