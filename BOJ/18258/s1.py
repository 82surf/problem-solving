from collections import deque
import sys
input = sys.stdin.readline

q = deque()
N = int(input())
for _ in range(N):
    command_li = input().split()
    opr = command_li[0]
    if opr == 'push':
        q.append(command_li[1])
    elif opr == 'pop':
        print(q.popleft()) if q else print(-1)
    elif opr == 'size':
        print(len(q))
    elif opr == 'empty':
        print(0) if q else print(1)
    elif opr == 'front':
        print(q[0]) if q else print(-1)
    else:
        print(q[-1]) if q else print(-1)
