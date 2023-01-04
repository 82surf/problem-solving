import sys
sys.stdin = open('input.txt')

# 종이의 가로, 세로 입력받기
W, H = map(int, input().split())

# x, y 좌표 입력받기
x, y = [0], [0]
T = int(input())
for _ in range(T):
    isHeight, n = map(int, input().split())
    x.append(n) if isHeight else y.append(n)
x.append(W)
y.append(H)
x.sort()
y.sort()

# 좌표쌍 정리
coordinates = []
for i in x:
    temp = []
    for j in y:
        temp.append((i, j))
    coordinates.append(temp)

# 넓이 계산
sizes = []
for i in range(len(coordinates) - 1):
    c1, c2 = coordinates[i], coordinates[i+1]
    for j in range(len(c1) - 1):
        a, b = c1[j], c2[j+1]
        size = (b[0] - a[0]) * (b[1] - a[1])
        sizes.append(size)

print(max(sizes))