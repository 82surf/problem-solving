import sys
input = sys.stdin.readline

N = int(input())
meeting_arr = [tuple(map(int, input().split())) for _ in range(N)]
meeting_arr.sort(key=lambda x: (x[1], x[0]))

answer = 1
end_time = meeting_arr[0][1]
for i in range(1, N):
    if meeting_arr[i][0] >= end_time:
        answer += 1
        end_time = meeting_arr[i][1]
print(answer)