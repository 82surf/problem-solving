# 시간초과
# 그리디
def solution(cap, n, deliveries, pickups):
    total_distance = 0
    d_sum, p_sum = sum(deliveries), sum(pickups)

    def go(arr, last_idx):
        space = cap
        # 가장 멀리 간 인덱스, 탐색을 마친 인덱스
        max_dist, min_dist = 0, 0
        # 처리 개수
        amount = 0
        # 뒤부터 최대한 적재 & 배달
        for i in range(last_idx, -1, -1):
            if arr[i]:
                if max_dist < i:
                    max_dist = i
                if arr[i] <= space:
                    space -= arr[i]
                    amount += arr[i]
                    arr[i] = 0
                else:
                    arr[i] -= space
                    amount += space
                    min_dist = i
                    break
        return max_dist, min_dist, amount

    # 모든 배달과 수거를 마치면 반복 종료
    while d_sum or p_sum:
        last_idx = n - 1
        # 배달 & 수거
        d_max_dist, d_min_dist, d_amount = go(deliveries, last_idx)
        p_max_dist, p_min_dist, p_amount = go(pickups, last_idx)
        # 배달, 수거 중 더 멀리 간 거리 확인
        dist = d_max_dist if d_max_dist > p_max_dist else p_max_dist
        # 배달, 수거를 마친 인덱스 확인
        last_idx = d_min_dist if d_min_dist > p_min_dist else p_min_dist
        # 이동 거리 적용
        total_distance += (dist + 1) * 2
        # 배달, 수거 개수 적용
        d_sum -= d_amount
        p_sum -= p_amount

        # print(f'd_max_dist, d_min_dist, d_amount: {d_max_dist, d_min_dist, d_amount}')
        # print(f'p_max_dist, p_min_dist, p_amount: {p_max_dist, p_min_dist, p_amount}')
        # print(f'deliveries: {deliveries}')
        # print(f'pickups: {pickups}')
        # print()

    return total_distance