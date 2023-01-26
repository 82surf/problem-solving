# 반복문으로 더해가면서 구하기

n = int(input())
arr = [0 for _ in range(n+1)]
arr[1] = 1
for i in range(2, n+1):
    arr[i] = arr[i-1] + arr[i-2]
print(arr[-1])
