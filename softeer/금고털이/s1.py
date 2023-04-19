import sys
input = sys.stdin.readline

W, N = map(int, input().split())
jewel_list = [list(map(int, input().split())) for _ in range(N)]
jewel_list.sort(key=lambda x: x[1], reverse=True)

answer = 0
for amount, val in jewel_list:
    if W >= amount:
        W -= amount
        answer += val * amount
    else:
        answer += val * W
        break

print(answer)