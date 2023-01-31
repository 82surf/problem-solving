# weight: cnt 형태로 저장하는 dict를 순회하며 조건을 만족하는 쌍 찾기
# 시간초과는 피했으나 테스트케이스 거의 다 틀림. 왜...?

def solution(weights):
    answer = 0
    w_cnt = {}

    for w in weights:
        if w in w_cnt:
            w_cnt[w] += 1
        else:
            w_cnt[w] = 1

    for w in w_cnt:
        cnt = w_cnt[w]
        conditions = [w * 1.5, w * 2, w * 4 / 3]
        if cnt:
            if cnt >= 2:
                answer += 1
            for c in conditions:
                if c <= 1001 and c == int(c) and int(c) in w_cnt:
                    answer += 1

    return answer
