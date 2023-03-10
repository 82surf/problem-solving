# find 최적화 & union 최적화

import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('input.txt')
input = sys.stdin.readline


# find 최적화
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


# union by rank
def union(a, b):
    a, b = find(a), find(b)

    if a == b:
        return
    elif rank[a] > rank[b]:
        parent[b] = a
        rank[a] += rank[b]
    else:
        parent[a] = b
        rank[b] += rank[a]


# 노드의 개수, 연산의 개수
n, m = map(int, input().split())

# 부모 배열
parent = [i for i in range(n + 1)]

# 트리의 높이를 기록하는 배열
rank = [1 for _ in range(n + 1)]

for _ in range(m):
    code, a, b = map(int, input().split())

    if code == 0:
        union(a, b)
    else:
        print('YES' if find(a) == find(b) else 'NO')

