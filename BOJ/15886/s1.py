N = int(input())
road = input()

answer = 0
for i in range(len(road)-1):
    if road[i] == 'E' and road[i+1] == 'W':
        answer += 1
print(answer)