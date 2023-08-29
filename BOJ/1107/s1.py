# TypeError
import sys
sys.stdin = open('input.txt')

N = input()
M = int(input())
keypad = dict.fromkeys(range(10))
if M:
    for broken in list(map(int, input().split())):
        keypad.pop(broken)


# 현재 위치에서 +, -로 이동 시 횟수
def only_use_plus_minus():
    return abs(int(N) - 100)


# 숫자 패드도 함께 이용 시 횟수
def use_keypad():
    target_channel_str = N
    target_channel_int = int(N)
    digit = 10 ** (len(target_channel_str) - 1)

    click_cnt = 0

    # 해당 숫자가 있으면 사용
    while digit > 0:
        target_n = int(target_channel_str[0])
        if target_n in keypad:
            target_channel_int -= digit * target_n
            click_cnt += 1
            digit //= 10
            target_channel_str = target_channel_str[1:]
        else:
            break

    # 해당 숫자가 없으면 (현재 자리수 * 버튼 - 남은 수)의 절댓값이 최소가 되게 하는 버튼 찾기
    while digit > 0:
        val = None
        min_abs_val = 500001
        for button in keypad.keys():
            tmp = digit * button
            abs_val = abs(target_channel_int - tmp)
            if min_abs_val > abs_val:
                min_abs_val = abs_val
                val = tmp
        # 해당 버튼 * 자리수를 타겟 채널에서 빼기
        target_channel_int -= val

        # 버튼 누른 횟수 카운트
        click_cnt += 1
        # 자리수 줄이기
        digit //= 10

    return abs(target_channel_int) + click_cnt


print(min(only_use_plus_minus(), use_keypad()))
