def solution(files):
    # HEAD, NUMBER, 순서 정보로 변환
    def parse(idx, file):
        parsed_file = []
        head_len = 0

        # HEAD 저장
        for i, c in enumerate(file):
            if c.isdigit():
                head_len = i
                break
        parsed_file.append(file[:head_len].upper())

        # NUMBER 저장
        number_end = len(file)
        for i in range(head_len, len(file)):
            c = file[i]
            if not c.isdigit():
                number_end = i
                break
        parsed_file.append(int(file[head_len:number_end]))

        return {"sort_data": parsed_file, "origin": file, "idx": idx}

    answer = []
    parsed_files = list(map(lambda x: parse(x[0], x[1]), enumerate(files)))
    parsed_files.sort(key=lambda x: (x['sort_data'][0], x['sort_data'][1], x['idx']))
    for data in parsed_files:
        answer.append(data['origin'])
    return answer