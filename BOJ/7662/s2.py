# 우선순위 큐 2개 사용
# 다른 큐에서 삭제된 노드를 저장하는 해시맵을 사용해 동기화하는 방식
# 마지막 출력 전 삭제된 노드를 모두 버리고 출력

from heapq import heappush, heappop
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())

    hq_id = 0
    min_hq = []
    max_hq = []

    deleted_n = {}

    def I(n):
        global hq_id

        heappush(min_hq, (n, hq_id))
        heappush(max_hq, (-n, hq_id))
        hq_id += 1

    def D(flag):
        hq = {-1: min_hq, 1: max_hq}
        flush(hq[flag])
        if hq[flag]:
            val, id = heappop(hq[flag])
            deleted_n[id] = 1

    def flush(hq):
        while hq and hq[0][1] in deleted_n:
            heappop(hq)


    for _ in range(k):
        operator, val = input().split()
        val = int(val)

        if operator == 'I':
            I(val)
        else:
            D(val)

    flush(min_hq)
    flush(max_hq)

    if max_hq:
        print(-max_hq[0][0], min_hq[0][0])
    else:
        print("EMPTY")

