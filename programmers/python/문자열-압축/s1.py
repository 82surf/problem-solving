# n개 단위로 글자 자르기
# 압축하기

def cut(s, n):
    result = []
    for i in range(0, len(s), n):
        part = s[i:i + n]
        result.append(part)
    return result


def compress(arr):
    result = ''
    cnt = 0
    curr = ''
    for s in arr:
        if curr != s:
            if cnt <= 1:
                result += curr
            else:
                result += str(cnt) + curr
            curr = s
            cnt = 1
        else:
            cnt += 1

    if cnt <= 1:
        result += curr
    else:
        result += str(cnt) + curr

    return result


def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        cuts = cut(s, i)
        result = compress(cuts)
        if answer > len(result):
            answer = len(result)
    return answer