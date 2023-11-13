def n_to_k(n, k):
    result = ''
    while n:
        r = n % k
        result = str(r) + result
        n //= k
    return result


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


def solution(n, k):
    answer = 0
    candidates = n_to_k(n, k).split('0')

    for c in candidates:
        if c != '' and is_prime(int(c)):
            answer += 1
    return answer