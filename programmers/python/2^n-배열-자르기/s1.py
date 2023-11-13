def solution(n, left, right):
    start, start_r = left // n, left % n
    end = right // n
    end_r = (end + 1) * n - right

    arr = []
    for i in range(start+1, end+2):
        for _ in range(i):
            arr.append(i)
        for j in range(i+1, n+1):
            arr.append(j)

    return arr[start_r:len(arr)-end_r+1]