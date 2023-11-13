def solution(x):
    total = 0
    num = x
    while num:
        total += num % 10
        num -= num % 10
        num /= 10
    if x % total:
        return False
    else:
        return True