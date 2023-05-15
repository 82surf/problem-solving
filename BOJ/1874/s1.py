import sys
input = sys.stdin.readline


n = int(input())
arr = [int(input()) for _ in range(n)]
target_idx = 0
val = 1
stack = [0]
result = []
is_possible = True

while target_idx < n and stack :
    target = arr[target_idx]
    if not stack or stack[-1] < target:
        stack.append(val)
        val += 1
        result.append('+')
    elif stack[-1] == target:
        target_idx += 1
        stack.pop()
        result.append('-')
    else:
        is_possible = False
        break

if is_possible:
    for opr in result:
        print(opr)
else:
    print('NO')
