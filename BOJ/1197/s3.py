"""
유형: 최소 비용 신장 트리
변경 풀이: 크루스칼 사용
"""

import sys
sys.stdin = open('input.txt')


# path compression
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


# union by size
def union(x, y):
    a, b = find(x), find(y)

    if size[a] < size[b]:
        a, b = b, a

    parent[b] = a
    size[a] += size[b]


def kruskal():
    edges = []
    for _ in range(E):
        edges.append(list(map(int, input().split())))
    edges.sort(key=lambda x: x[2])

    total = 0
    cnt = 0
    for n1, n2, w in edges:
        if find(n1) != find(n2):
            cnt += 1
            total += w
            union(n1, n2)
            if cnt == V:
                break

    return total


V, E = map(int, input().split())

parent = [i for i in range(V + 1)]
size = [1 for _ in range(V + 1)]

print(kruskal())