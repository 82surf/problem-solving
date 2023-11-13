# 최대힙, 최소힙
# 삭제한 값을 저장하는 해시테이블

from heapq import heappush, heappop


def solution(operations):
    max_hq = []
    min_hq = []
    deleted = {}
    num_id = 0

    def flush(arr):
        while arr and arr[0][2] in deleted:
            heappop(arr)

    def insert(n):
        nonlocal num_id

        heappush(max_hq, (-n, n, num_id))
        heappush(min_hq, (n, n, num_id))
        num_id += 1

    def delete(flag):
        target = {1: max_hq, -1: min_hq}
        hq = target[flag]
        flush(hq)
        if hq:
            priority, num, n_id = heappop(hq)
            deleted[n_id] = None

    for string in operations:
        operation, val = string.split()
        val = int(val)

        if operation == 'I':
            insert(val)
        elif operation == 'D':
            delete(val)

    flush(max_hq)
    flush(min_hq)

    if max_hq:
        return [max_hq[0][1], min_hq[0][1]]
    else:
        return [0, 0]
