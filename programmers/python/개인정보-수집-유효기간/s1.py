def solution(today, terms, privacies):
    answer = []
    today_li = list(map(int, today.split(".")))

    # 약관 별 만료 기간 객체 생성
    terms_dic = {}
    for t in terms:
        key, val = t.split(" ")
        terms_dic[key] = int(val)

    for i, privacy in enumerate(privacies):
        # 날짜, 약관 추출
        date, key = privacy.split(" ")
        expire_li = list(map(int, date.split(".")))

        # 만료 날짜로 변경
        expire_li[1] += terms_dic[key]
        if expire_li[1] > 12:
            remain = expire_li[1] % 12
            share = expire_li[1] // 12
            if not remain:
                expire_li[1] = 12
                expire_li[0] += share - 1
            else:
                expire_li[1] = remain
                expire_li[0] += share

        # 만료 여부 확인
        for j in range(3):
            if today_li[j] < expire_li[j]:
                break
            elif today_li[j] == expire_li[j]:
                if j == 2:
                    answer.append(i + 1)
                    break
            else:
                answer.append(i + 1)
                break

    return answer
