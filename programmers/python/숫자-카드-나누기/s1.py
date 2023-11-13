from math import gcd


def ngcd(arr):
    result = arr[0]
    for n in arr:
        result = gcd(result, n)
    return result


def check(arr, gcd):
    for n in arr:
        if n % gcd == 0:
            return 0
    return gcd


def solution(arrayA, arrayB):
    gcdA, gcdB = check(arrayB, ngcd(arrayA)), check(arrayA, ngcd(arrayB))
    return max(gcdA, gcdB)