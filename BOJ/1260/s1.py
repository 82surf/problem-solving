import sys
sys.stdin = open('input.txt')


def DFS(s):
    visited = [0 for _ in range(N + 1)]
    stack = [s]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            next_v_arr = []
            for next_v in arr[v]:
                next_v_arr.append(next_v)
            next_v_arr.sort(reverse=True)
            stack += next_v_arr


def BFS(s):
    visited = [0 for _ in range(N + 1)]
    visited[s] = 1
    q = [s]
    while q:
        v = q.pop(0)
        print(v, end=' ')
        next_v_arr = []
        for next_v in arr[v]:
            if not visited[next_v]:
                visited[next_v] = 1
                next_v_arr.append(next_v)
        next_v_arr.sort()
        q += next_v_arr


N, M, V = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

DFS(V)
print()
BFS(V)
