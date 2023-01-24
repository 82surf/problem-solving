from collections import deque
from heapq import heappush, heappop


def solution(jobs):
    # (소요시간, 요청시각) 튜플을 원소로 하는 배열 생성 후 정렬 (소요시간 기준 최소 합을 만들기 위해)
    tasks = deque(sorted([(job[1], job[0]) for job in jobs], key=lambda x: (x[1], x[0])))

    # 대기 중인 작업 우선순위 큐
    q = []
    heappush(q, tasks.popleft())

    # 현재 시각, 총 소요 시간
    curr_t, total = 0, 0

    while q:
        # 현재 작업의 소요 시간, 요청 시각
        dur, req_t = heappop(q)
        # 종료 시각으로 이동
        curr_t = max(curr_t + dur, req_t + dur)
        # 총 소요 시간 계산
        total += curr_t - req_t

        # 종료 시각까지 요청받은 작업 대기 큐에 추가
        while tasks and tasks[0][1] <= curr_t:
            heappush(q, tasks.popleft())

        # 작업 대기 큐가 비어있다면 먼저 요청이 들어온 작업 추가
        if tasks and not q:
            heappush(q, tasks.popleft())

    return total // len(jobs)