# 완전탐색(순열)풀이
# 최대로 걸린 Test: 통과 (8069.48ms, 10.4MB)
# 다이아, 철, 돌 => 0, 1, 2로 변환
def mineral_to_num(mineral):
    dic = {'diamond': 0, 'iron': 1, 'stone': 2}
    return dic[mineral]


def solution(picks, minerals):
    # 피로도
    fatigue_table = [
        [1, 1, 1],
        [5, 1, 1],
        [25, 5, 1]
    ]

    # minerals 배열 숫자로 변환
    num_minerals = list(map(mineral_to_num, minerals))

    # 최소 피로도
    answer = float('inf')

    # 곡괭이를 사용하는 경우의 수(순열)
    def permutations(picks, result=[]):
        nonlocal answer

        # 재귀 종료
        if not sum(picks):
            # 광물 배열 순회 인덱스
            idx = 0
            # 총 피로도
            fatigue = 0
            # 곡괭이 배열 순회
            for pick in result:
                no_minerals = False
                for _ in range(5):
                    if idx == len(num_minerals):
                        no_minerals = True
                        break
                    mineral = num_minerals[idx]
                    fatigue += fatigue_table[pick][mineral]
                    idx += 1
                if no_minerals:
                    break
            if answer > fatigue:
                answer = fatigue
            return

        for i, n in enumerate(picks):
            if n:
                curr_picks = picks.copy()
                curr_picks[i] -= 1

                curr_result = result.copy()
                curr_result.append(i)
                permutations(curr_picks, curr_result)

    permutations(picks)

    return answer