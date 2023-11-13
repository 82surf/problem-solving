# 10진수를 n진법 문자열로 반환하는 함수
def dec_to_n(num: int, n: int) -> str:
    if not num:
        return '0'
    result = ''
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while num:
        remainder = num % n
        remainder = str(remainder) if remainder < 10 else dic[remainder]
        num //= n
        result = remainder + result
    return result


def solution(n, t, m, p):
    # 최대 문자열 길이
    max_len = (t - 1) * m + p

    # 최대 문자열 길이보다 커질 때까지 n진법 문자열 더하기
    n_str = ''
    curr_num = -1
    while len(n_str) < max_len:
        curr_num += 1
        n_str += dec_to_n(curr_num, n)

    # p 순서 기록
    answer = ''
    idx, cnt = p - 1, t
    while t:
        answer += n_str[idx]
        idx += m
        t -= 1
    return answer