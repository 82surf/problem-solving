import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

S = {}


def add(x):
    if x not in S:
        S[x] = 1


def remove(x):
    if x in S:
        S.pop(x)


def check(x):
    print(1) if x in S else print(0)


def toggle(x):
    if x in S:
        S.pop(x)
    else:
        S[x] = 1


def all():
    global S
    S = dict.fromkeys(range(1, 21))


def empty():
    global S
    S = {}


mapper_a = {
    'add': add,
    'remove': remove,
    'check': check,
    'toggle': toggle,
}

mapper_b = {
    'all': all,
    'empty': empty
}

M = int(input())
for _ in range(M):
    string = input().rstrip()
    if string in mapper_b:
        mapper_b[string]()
    else:
        command, x = string.split()
        mapper_a[command](int(x))
