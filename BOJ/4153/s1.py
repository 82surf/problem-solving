import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    a2, b2, c2 = a ** 2, b ** 2, c ** 2

    t1 = a2 == b2 + c2
    t2 = b2 == a2 + c2
    t3 = c2 == a2 + b2

    if t1 or t2 or t3:
        print('right')
    else:
        print('wrong')