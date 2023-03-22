# 투 포인터
# 해설 보고 품

def solution(queue1, queue2):
    q = queue1 + queue2
    total = sum(q)
    if total % 2:
        return -1

    target = total // 2
    curr = sum(queue1)
    s, e = 0, len(queue1) - 1
    answer = 0

    while s < len(q) and e < len(q):
        if curr == target:
            return answer
        elif curr < target and e < len(q) - 1:
            e += 1
            curr += q[e]
            answer += 1
        else:
            curr -= q[s]
            s += 1
            answer += 1

    return -1