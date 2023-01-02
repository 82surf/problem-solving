import sys
sys.stdin = open('input.txt')

for _ in range(int(input())):
    R, S = input().split()
    ans = ''
    for c in S:
        ans += c * int(R)
    print(ans)