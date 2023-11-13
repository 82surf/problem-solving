def solution(k, tangerine):
    N = max(tangerine)
    cnt = [0] * (N + 1)
    for t in tangerine:
        cnt[t] += 1
    cnt.sort(reverse=True)

    answer = 0
    for c in cnt:
        if k <= 0:
            break
        k -= c
        answer += 1

    return answer
