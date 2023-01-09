# 새로운 풀이
# f(n+1) = f(n) + 1 + f(n)
# 2번째 단계에서는 2개의 원판을 3번째 타워로 옮긴다.
# 3번째 단계에서는 2개의 원판을 2번째 타워로 옮긴다. => f(n)
# 3번째 원판을 3번째 타워로 옮긴다 => 1
# 2번째 타워에 있는 2개의 원판을 3번째 타워로 옮긴다 => f(n)
# 따라서 하노이 탑의 최소 이동 개수는 f(n+1) = f(n) + 1 + f(n)을 만족한다.
# 여기서 수행 과정을 촐력하려면 수행 과정이 변하는 규칙을 추가로 찾아야 한다. 그리고 재귀로 구현하면 될 듯!

def change_2_and_3(n):
    if n == 2:
        return 3
    elif n == 3:
        return 2
    else:
        return n


def add_1(n):
    result = n + 1
    return result if result < 4 else 1


def hanoi_route(n):
    if n == 1:
        return [[1, 3]]
    else:
        before = hanoi_route(n - 1)
        a = list(map(lambda x: list(map(change_2_and_3, x)), before))
        b = list(map(lambda x: list(map(add_1, x)), a))
        return a + [[1, 3]] + b


def hanoi_cnt(n):
    if n == 1:
        return 1
    else:
        return hanoi_cnt(n - 1) * 2 + 1

N = int(input())
print(hanoi_cnt(N))
if N <= 20:
    routes = hanoi_route(N)
    for r in routes:
        print(' '.join(map(str, r)))