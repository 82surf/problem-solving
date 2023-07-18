n = int(input())
answer = 1
for i in range(n-1):
    answer = (answer * 2) - 1 if i % 2 else (answer * 2) + 1
print(answer % 10007)