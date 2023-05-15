import sys
input = sys.stdin.readline


def is_valid(ps):
    stack = []
    for p in ps:
        if not stack:
            stack.append(p)
        elif stack[-1] == '(' and p == ')':
            stack.pop()
        else:
            stack.append(p)
    return len(stack) == 0


T = int(input())
for _ in range(T):
    print('YES') if is_valid(input().rstrip()) else print('NO')