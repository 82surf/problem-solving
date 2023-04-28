from collections import deque


def check(x):
    for i, n in enumerate(q):
        if x == n:
            return len(q) // 2 >= i


def pop(x):
    if check(x):
        while q[0] != x:
            move_left()
        q.popleft()
    else:
        while q[0] != x:
            move_right()
        q.popleft()


# 2번 연산
def move_left():
    global answer
    q.append(q.popleft())
    answer += 1


# 3번 연산
def move_right():
    global answer
    q.appendleft(q.pop())
    answer += 1


N, M = map(int, input().split())
targets = list(map(int, input().split()))
q = deque(range(1, N+1))
answer = 0

for t in targets:
    pop(t)

print(answer)