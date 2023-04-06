def solution(k, d):
    max_n = d ** 2
    answer = 0
    for i in range(0, d + 1, k):
        calc = int((max_n - i ** 2) ** 0.5)
        answer += calc // k + 1
    return answer