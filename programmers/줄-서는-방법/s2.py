# TC, 효율성 모두 통과

# n 팩토리얼 값을 구하는 함수
def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n - 1)


# 재귀적으로 k번째 방법을 만드는 함수
def recursive(n, k, answer, visited, idx):
    fac = factorial(n - 1)
    share = k // fac if fac else 0
    nxt_k = k - (share * fac)

    # 사용하지 않은 수 탐색
    # share번째 수를 answer에 입력
    cnt = share + 1
    for i, v in enumerate(visited):
        if not v and cnt:
            cnt -= 1
        if not v and not cnt:
            answer[idx] = i
            visited[i] = 1
            break

    if n == 0:
        return answer
    return recursive(n - 1, nxt_k, answer, visited, idx + 1)


# main 함수
def solution(n, k):
    # 정답 배열
    answer = [0] * n
    # 사용한 수를 확인하는 배열
    visited = [0] * (n + 1)
    # 0은 사용하지 않도록 방문 처리
    visited[0] = 1

    # k - 1로 시작하는 이유
    # n!의 몪으로 구간이 나눠지게 되는데, k로 진행하면 경계값이 하나 잘못 나오게 된다.
    # 경계값이 올바르게 들어가도록 k번을 셀 때 0부터 셈
    return recursive(n, k - 1, answer, visited, 0)