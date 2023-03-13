from itertools import combinations

def solution(orders, course):
    # orders 원소 정렬
    orders = list(map(sorted, orders))
    # 손님 주문 별 조합 생성
    menus = {}
    for order in orders:
        for i in range(2, len(orders) + 1):
            for c in combinations(order, i):
                # dict에 조합별 주문 횟수 카운트
                key = ''.join(c)
                if key in menus:
                    menus[key] += 1
                else:
                    menus[key] = 1
    # 2번 이상 주문된 메뉴 중 가장 많이 주문된 메뉴
    courses = {n: [] for n in course}
    for menu, cnt in menus.items():
        if cnt > 1 and len(menu) in course:
            if not courses[len(menu)] or courses[len(menu)][0][1] == cnt:
                courses[len(menu)].append((menu, cnt))
            elif courses[len(menu)][0][1] < cnt:
                courses[len(menu)] = [(menu, cnt)]
    # 정답 기록
    answer = []
    for li in courses.values():
        for m, cnt in li:
            answer.append(m)
    return sorted(answer)