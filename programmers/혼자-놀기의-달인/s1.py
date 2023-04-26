def solution(cards):
    is_open = [0] * len(cards)

    def open_box(start):
        card_idx = start
        cnt = 0
        while is_open[card_idx] == 0:
            is_open[card_idx] = 1
            card_idx = cards[card_idx] - 1
            cnt += 1
        return cnt

    answer = []
    while True:
        for idx, opened in enumerate(is_open):
            if not opened:
                cnt = open_box(idx)
                answer.append(cnt)
                break
        else:
            break

    if len(answer) == 1:
        return 0
    else:
        answer.sort(reverse=True)
        return answer[0] * answer[1]
