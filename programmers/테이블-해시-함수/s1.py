def solution(data, col, row_begin, row_end):
    sorted_data = sorted(data, key=lambda x: (x[col - 1], -x[0]))
    s_arr = []
    for i in range(row_begin - 1, row_end):
        row = sorted_data[i]
        s = 0
        for n in row:
            s += n % (i + 1)
        s_arr.append(s)

    answer = s_arr[0]
    for i in range(1, len(s_arr)):
        answer ^= s_arr[i]
    return answer