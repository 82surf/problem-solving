# 시간초과
# 가장 기본적인 union find

import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find_parent(x, parent):
    if x != parent[x]:
        return find_parent(parent[x], parent)
    return x


def union(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수, 연산의 개수
n, m = map(int, input().split())

# 부모 배열
parent = [i for i in range(n + 1)]

for _ in range(m):
    code, a, b = map(int, input().split())

    if code == 0:
        union(a, b, parent)
    else:
        print('YES' if find_parent(a, parent) == find_parent(b, parent) else 'NO')