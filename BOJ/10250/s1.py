import sys
sys.stdin = open('input.txt')


def solution(H, N):
    if N % H:
        XX = N // H + 1
        YY = N % H
    else:
        XX = N // H
        YY = H
    return str(YY) + str(XX).zfill(2)



T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    print(solution(H, N))