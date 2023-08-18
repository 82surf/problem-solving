import math

N = int(input())
num = str(math.factorial(N))
idx = len(num) - 1
answer = 0
while num[idx] == '0':
    answer += 1
    idx -= 1
print(answer)