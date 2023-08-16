check = [0] * 1000
for _ in range(10):
    n = int(input())
    check[n % 42] = 1
print(sum(check))