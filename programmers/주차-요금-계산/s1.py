from math import ceil
from datetime import datetime


def solution(fees, records):
    car_records = {}

    # 누적 주차 시간(초)를 입력받으면 주차 요금 반환
    def calc_fee(sec):
        default_time, default_fee, unit_time, unit_fee = fees
        m = sec // 60

        if default_time >= m:
            return default_fee
        else:
            extra_time = m - default_time
            return default_fee + ceil(extra_time / unit_time) * unit_fee

    # 입출차 기록 순회하며 총 시간 기록
    cars = [0] * 10000
    for record in records:
        t, car_n, record_type = record.split()
        t = datetime.strptime(t, "%H:%M")
        car_n = int(car_n)

        if cars[car_n]:
            if cars[car_n]["in_out_record"]:
                before_t = cars[car_n]["in_out_record"].pop()
                cars[car_n]["total_time"] += (t - before_t).seconds
            else:
                before_t = cars[car_n]["in_out_record"].append(t)
        else:
            car_record = {
                "in_out_record": [t],
                "total_time": 0
            }
            cars[car_n] = car_record

    # 입차 기록만 남아있는 경우 총 시간 추가
    for car in cars:
        if car and car["in_out_record"]:
            last_in = car["in_out_record"][-1]
            car["total_time"] += (datetime.strptime("23:59", "%H:%M") - last_in).seconds

    # 요금 계산
    answer = []
    for car in cars:
        if car:
            answer.append(calc_fee(car["total_time"]))
    return answer