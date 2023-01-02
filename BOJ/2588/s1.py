import sys
sys.stdin = open('input.txt')

a, b = int(input()), input()
b_int, b_arr = int(b), list(map(int, list(b)))

for i in range(2, -1, -1):
    print(a * b_arr[i])

print(a * b_int)