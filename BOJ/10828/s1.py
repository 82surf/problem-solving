import sys
input = sys.stdin.readline

stack = []
N = int(input())
for _ in range(N):
    command_li = input().split()
    opr = command_li[0]
    if opr == 'push':
        stack.append(int(command_li[1]))
    elif opr == 'pop':
        print(stack.pop()) if stack else print(-1)
    elif opr == 'size':
        print(len(stack))
    elif opr == 'empty':
        print(0) if stack else print(1)
    else:
        print(stack[-1]) if stack else print(-1)
