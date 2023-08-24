from collections import deque
import sys
sys.stdin = open('input.txt')


def BFS(n, k):
    q = deque([(n, 0, 0)])
    visited = [0] * 100001
    visited[n] = 1

    while q:
        x, before_action, cnt = q.popleft()
        if x == k:
            return cnt

        for val in [2, 1, -1]:
            next_x = x
            if val == 2:
                next_x *= val
            else:
                next_x += val

            if 0 <= next_x <= 100000 and not visited[next_x]:
                visited[next_x] = 1
                q.append((next_x, val, cnt + 1))


print(BFS(*map(int, input().split())))
