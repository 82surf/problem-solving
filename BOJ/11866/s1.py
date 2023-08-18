from collections import deque
import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
q = deque(list(range(1, N + 1)))


def cycle():
    for _ in range(K - 1):
        q.append(q.popleft())
    return q.popleft()


print('<', end='')
while q:
    if len(q) > 1:
        print(str(cycle()) + ',', end=' ')
    else:
        print(q.popleft(), end='')
print('>')