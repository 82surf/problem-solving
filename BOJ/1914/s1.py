# 실패한 풀이
# 의미 없이 반복하는 수가 많아 최대 재귀 깊이 초과, 백트래킹도 실패

def solution(tower, cnt, record, result):
    global min_cnt
    print(min_cnt)
    if cnt > min_cnt:
        return
    print(f'cnt: {cnt}')
    if tower[2] == result:
        print(cnt)
        min_cnt = cnt
        if N <= 20:
            for i in range(cnt):
                print(record[i])
    else:
        for i in range(3):
            if tower[i]:
                n = tower[i].pop()
                print(f'n: {n}')
                for j in range(3):
                    print(f'j: {j}')
                    if i != j:
                        print('first if')
                        if not tower[j] or (tower[j] and tower[j][-1] > n):
                            print('second if')
                            if not record or (record and (j, i) != record[-1]):
                                print('third if')
                                tower[j].append(n)
                                record.append((i, j))
                                print(tower)
                                print(record)
                                solution(tower, cnt + 1, record, result)


min_cnt = 999999999999
N = int(input())
completed = [i for i in range(N, 0, -1)]
solution([completed[:], [], []], 0, [], completed[:])