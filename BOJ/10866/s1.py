from collections import deque
import sys
input = sys.stdin.readline

q = deque()
N = int(input())


def push_front(val):
    q.appendleft(val)


def push_back(val):
    q.append(val)


def pop_front():
    print(q.popleft()) if q else print(-1)


def pop_back():
    print(q.pop()) if q else print(-1)


def size():
    print(len(q))


def empty():
    print(0) if q else print(1)


def front():
    print(q[0]) if q else print(-1)


def back():
    print(q[-1]) if q else print(-1)


commands = {
    'push_front': push_front,
    'push_back': push_back,
    'pop_front': pop_front,
    'pop_back': pop_back,
    'size': size,
    'empty': empty,
    'front': front,
    'back': back,
}

for _ in range(N):
    command_li = input().split()
    opr = command_li[0]
    if opr == 'push_front' or opr == 'push_back':
        commands[opr](command_li[1])
    else:
        commands[opr]()