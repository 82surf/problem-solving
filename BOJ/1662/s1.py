import sys
sys.stdin = open('input.txt')

compressed = list(input())

while True:
    start, end = -1, -1
    for i in range(len(compressed) - 1, -1, -1):
        if compressed[i] == '(':
            start = i + 1
            break
    for i in range(start, len(compressed)):
        if compressed[i] == ')':
            end = i
            break
    result = compressed[start:end] * int(compressed[start - 2])
    compressed = compressed[:start - 2] + result + compressed[end + 1:]

    if '(' not in compressed:
        break

print(len(compressed))
