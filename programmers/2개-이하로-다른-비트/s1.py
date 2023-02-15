# 시간초과
# numbers의 각 수가 최대 10^15인데 이진수 비교가 O(N)

def solution(numbers):
    # 두 수를 이진수로 변환 후 다른 수가 2개 이하인지 확인
    def check_diff(a, b):
        bin_a, bin_b = bin(a)[2:], bin(b)[2:]
        l = max(len(bin_a), len(bin_b))
        bin_a = str(bin_a).zfill(l)
        bin_b = str(bin_b).zfill(l)
        cnt = 0
        for i in range(l):
            if bin_a[i] != bin_b[i]:
                cnt += 1
            if cnt > 2:
                return False
        return True

    # 자신보다 큰 수 중 조건을 만족하는 수를 반환
    def func(x):
        min_n = x + 1
        while not check_diff(min_n, x):
            min_n += 1
        return min_n

    # numbers를 순회하며 함수 반환값을 기록
    answer = [0] * len(numbers)
    for i, n in enumerate(numbers):
        answer[i] = func(n)
    return answer
