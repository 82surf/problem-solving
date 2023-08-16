while True:
    num = input()
    if num == '0':
        break
    r_num = num[::-1]

    if int(num) - int(r_num) == 0:
        print('yes')
    else:
        print('no')