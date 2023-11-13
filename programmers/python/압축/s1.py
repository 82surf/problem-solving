def solution(msg):
    # 사전 초기화
    dic = {}
    dic_idx = 0
    for i in range(65, 91):
        dic_idx += 1
        dic[chr(i)] = dic_idx

    # 문자열 순회하면서 출력
    answer = []
    start_idx, search_len = 0, 1
    while start_idx + search_len < len(msg) + 1:
        w = msg[start_idx:start_idx + search_len]
        if w in dic:
            next_w = msg[start_idx:start_idx + search_len + 1]
            search_len += 1
            if next_w not in dic or w == next_w:
                answer.append(dic[w])
        else:
            dic_idx += 1
            dic[w] = dic_idx
            start_idx += search_len - 1
            search_len = 1

    return answer