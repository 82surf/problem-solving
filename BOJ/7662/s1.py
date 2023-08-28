# 시간초과
# 우선순위 큐 2개를 사용해 구현
from heapq import heappush, heappop
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    min_hq = []
    max_hq = []

    # I 연산
    def I(n):
        heappush(min_hq, (n, n))
        heappush(max_hq, (-n, n))

    # D 연산
    def D(flag):
        dic = { 1: max_hq, -1: min_hq }
        if min_hq:
            priority, n = heappop(dic[flag])
            dic[-flag].remove((-priority, n))


    # 정답 출력부 구현
    k = int(input())
    for _ in range(k):
        operator, val = input().split()
        val = int(val)

        if operator == 'I':
            I(val)
        elif val == 1:
            D(1)
        else:
            D(-1)

    if min_hq:
        print(max_hq[0][1], min_hq[0][1])
    else:
        print('EMPTY')