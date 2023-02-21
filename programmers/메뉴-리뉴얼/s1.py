# 시간초과
from itertools import combinations


def solution(orders, course):
    # 등장하는 알파벳 종류 모으기
    def get_dishes(orders):
        dishes = set()
        for order in orders:
            for dish in order:
                dishes.add(dish)
        return sorted(list(dishes))

    dishes = get_dishes(orders)

    # 조합이 포함되어있는지 확인할 수 있도록 orders 원소를 set으로 변환
    orders = list(map(lambda x: set(list(x)), orders))

    # 정답 배열
    answer = []

    # courses 순회하면서 조합 객체 생성
    for n in course:
        courses = {}
        for c in combinations(dishes, n):
            cnt = 0
            for order in orders:
                if not set(c) - order:
                    cnt += 1
            if cnt:
                courses[c] = cnt

        # 2번 이상 등장한 조합 중 가장 많이 등장한 조합을 정답 배열에 추가
        curr_answer, max_cnt = [], 0
        for cr, cnt in courses.items():
            if max_cnt < cnt:
                curr_answer = [cr]
                max_cnt = cnt
            elif max_cnt == cnt:
                curr_answer.append(cr)
        if max_cnt >= 2:
            answer += list(map(lambda x: ''.join(x), curr_answer))

    # 정답 배열 정렬 후 반환
    return sorted(answer)