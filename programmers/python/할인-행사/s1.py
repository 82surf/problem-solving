def solution(want, number, discount):
    answer = 0

    # 원하는 품목 객체 초기화
    want_dic = {}
    for i in range(len(want)):
        item, amount = want[i], number[i]
        want_dic[item] = want_dic.get(item, 0) + amount

    # 첫 10일 간의 할인 정보 초기화
    discount_dic = {}
    for i in range(10):
        item = discount[i]
        discount_dic[item] = discount_dic.get(item, 0) + 1

    # 조건을 확인하는 함수
    def check():
        nonlocal answer
        for item, amount in want_dic.items():
            if item not in discount_dic:
                print(item)
                break
            elif amount > discount_dic[item]:
                break
        else:
            answer += 1

    check()

    # 구간 변경하면서 할인 정보 변경 후 조건 확인
    start, end = 0, 10
    while end < len(discount):
        # 품목 제거
        remove_item = discount[start]
        discount_dic[remove_item] -= 1
        # 품목 추가
        add_item = discount[end]
        discount_dic[add_item] = discount_dic.get(add_item, 0) + 1

        # 조건 확인
        check()

        start += 1
        end += 1

    return answer
