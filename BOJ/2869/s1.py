import math

A, B, V = map(int, input().split())
diff = A - B
print(math.ceil((V - A) / diff) + 1)