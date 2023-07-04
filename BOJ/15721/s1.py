import sys
sys.stdin = open('input.txt')

A = int(input())
T = int(input())
G = int(input())

a_cnt, b_cnt, d_cnt, cycle = -1, 0, 0, 1


def check():
    return b_cnt == T if G == 0 else d_cnt == T


def bbun():
    global a_cnt, b_cnt
    a_cnt += 1
    b_cnt += 1


def deggi():
    global a_cnt, d_cnt
    a_cnt += 1
    d_cnt += 1


def solution():
    global a_cnt, b_cnt, d_cnt, cycle
    while True:
        for _ in range(2):
            bbun()
            if check():
                return
            deggi()
            if check():
                return
        for _ in range(cycle + 1):
            bbun()
            if check():
                return
        for _ in range(cycle + 1):
            deggi()
            if check():
                return
        cycle += 1


solution()
print(a_cnt % A)
