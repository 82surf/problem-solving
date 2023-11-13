# 통과
# BFS를 사용해 최솟값 탐색
# visited 배열을 사용해 이미 탐색했던 노드는 더이상 탐색하지 않도록 가지치기

from collections import deque


def solution(x, y, n):
    def bfs(x, y, n):
        q = deque([x])
        visited = [0] * 1000001
        visited[x] = 1
        while q:
            val = q.popleft()
            if val == y:
                return visited[val] - 1
            next_vals = [val + n, val * 2, val * 3]
            for nv in next_vals:
                if nv <= y and not visited[nv]:
                    visited[nv] = visited[val] + 1
                    q.append(nv)
        return -1

    return bfs(x, y, n)