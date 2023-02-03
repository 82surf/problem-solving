def solution(msg):
    # 사전 초기화
    dic = {}
    dic_idx = 0
    for i in range(65, 91):
        dic_idx += 1
        dic[chr(i)] = dic_idx

    # 문자열을 순회하면서 사전 색인 생성
    N = len(msg)
    msg_idx = 0
    search_len = 1
    move = 0
    answer = []
    while True:
        w = msg[msg_idx:msg_idx + search_len]
        # print(f'msg_idx: {msg_idx} | w: {w} | msg_idx: {msg_idx} | search_len: {search_len} | move: {move}')
        if w in dic:
            search_len += 1
            move += 1
            if dic[w] not in answer:
                answer.append(dic[w])
            if msg_idx == N - 1:
                break
        else:
            dic_idx += 1
            dic[w] = dic_idx
            msg_idx += move
            search_len = 1
            move = 0

    # print(dic)
    return answer


print(solution('KAKAO'))
