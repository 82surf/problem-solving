def solution(n):
    if n < 100:
        return n
    else:
        han_nums = []
        for i in range(1, 10):
            arr = [i, 0, 0]
            for j in range(10):
                arr[1] = arr[0] + j
                arr[2] = arr[1] + j
                num = int(''.join(map(str, arr)))
                if num <= n:
                    han_nums.append(num)

                arr[1] = arr[0] - j
                arr[2] = arr[1] - j
                if arr[1] >= 0 and arr[2] >= 0:
                    num = int(''.join(map(str, arr)))
                    if num <= n and num not in han_nums:
                        han_nums.append(num)
        return len(han_nums) + 99

print(solution(int(input())))