# 맨 앞자리 수 처리를 추가하여 해결

def solution(storey):
    answer = 0
    arr = list(map(int, list(str(storey))))
    for i in range(len(arr) - 1, -1, -1):
        n = arr[i]
        if i == 0:
            if n > 5:
                answer += 10 - n + 1
            else:
                answer += n
        elif n > 5:
            answer += 10 - n
            arr[i - 1] += 1
        elif n == 5:
            if arr[i - 1] >= 5:
                answer += 10 - n
                arr[i - 1] += 1
            else:
                answer += n
        else:
            answer += n

    return answer