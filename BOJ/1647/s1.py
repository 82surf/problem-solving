import sys
input = sys.stdin.readline


# path compression
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    a, b = find(x), find(y)
    if size[a] < size[b]:
        a, b = b, a
    parent[b] = a
    size[a] += size[b]


def kruskal():
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])

    cnt = 0
    total = 0
    max_w = 0

    for a, b, w in edges:
        if find(a) != find(b):
            cnt += 1
            total += w
            if max_w < w:
                max_w = w
            union(a, b)
            if cnt == V:
                break

    return total, max_w


V, E = map(int, input().split())
parent = [i for i in range(V + 1)]
size = [1 for _ in range(V + 1)]

total, max_w = kruskal()
print(total-max_w)