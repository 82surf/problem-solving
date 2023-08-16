notes = list(map(int, input().split()))
asc = list(range(1, 9))
desc = list(range(8, 0, -1))

if notes == asc:
    print('ascending')
elif notes == desc:
    print('descending')
else:
    print('mixed')