def solution(numbers):
    # 다른 비트가 2개 이하인 가장 작은 수 만들기
    def get_num(n):
        bin_n = list(bin(n)[2:])  # 이진수 변환
        for i in range(len(bin_n) - 1, -1, -1):  # 뒤부터 순회
            if bin_n[i] == '0':  # 첫 0이 나오면
                bin_n[i] = '1'  # 해당 부분 1로 바꾸고
                if i + 1 < len(bin_n):  # 이전 1이 있다면 0으로 변경
                    bin_n[i + 1] = '0'
                break
        else:  # 끝까지 0이 나오지 않으면 맨 앞을 0으로 바꾸고 그 앞에 1을 추가
            bin_n[0] = '0'
            return int('1' + ''.join(bin_n), 2)
        return int(''.join(bin_n), 2)

    # numbers를 순회하며 함수 반환값을 기록
    answer = [0] * len(numbers)
    for i, n in enumerate(numbers):
        answer[i] = get_num(n)
    return answer

