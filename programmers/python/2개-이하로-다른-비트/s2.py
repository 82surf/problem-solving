# 시간초과
# 비트연산으로 변경했으나 시간초과

def solution(numbers):
    # XOR 연산으로 다른 비트를 찾고 개수 count
    def check_diff(a, b):
        xor = bin(a ^ b)
        print(xor)
        return True if xor.count('1') <= 2 else False

    # 자신보다 큰 수 중 조건을 만족하는 수를 반환
    def func(x):
        min_n = x + 1
        while not check_diff(min_n, x):
            min_n += 1
        return min_n
    print(func(72349))
    # # numbers를 순회하며 함수 반환값을 기록
    # answer = [0] * len(numbers)
    # for i, n in enumerate(numbers):
    #     answer[i] = func(n)
    # return answer

solution(1)

