def solution(n):
    # n이 속해있는 구간에서 1로만 시작하는 수가 몇인지 반환
    def search(n):
        part = 3
        tmp = 3
        cnt = 1
        while n > part:
            tmp *= 3
            part += tmp
            cnt += 1
        return part // 3, cnt

    # 3진법 배열 변환
    def to_ternary(diff, l):
        num = diff
        result = [0] * l
        idx = l - 1
        while num:
            result[idx] = num % 3
            num //= 3
            idx -= 1
        return result

    def parser(arr):
        dic = {0: '1', 1: '2', 2: '4'}
        for i in range(len(arr)):
            arr[i] = dic[arr[i]]
        return list(map(str, arr))

    start, cnt = search(n)
    diff = n - start
    ternary = to_ternary(diff, cnt)

    return ''.join(parser(ternary))