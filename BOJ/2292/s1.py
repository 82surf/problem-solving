# N번째 벌집이 몇겹째에 위치해 있는지 출력하는 문제
N = int(input())

answer = 1
cnt = 1
diff = 6
while N > cnt:
    cnt += diff
    diff += 6
    answer += 1
print(answer)