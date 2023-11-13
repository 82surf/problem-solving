# C# => c로 변환하는 함수
def process(s):
    result = list(s)
    for i, c in enumerate(result):
        if c == '#':
            result[i - 1] = result[i - 1].lower()
    return ''.join(result).replace('#', '')


def solution(m, musicinfos):
    # 멜로디 가공
    memory = process(m)

    # 음악에서 검색
    result = None
    for musicinfo in musicinfos:
        # 음악 정보
        start, end, title, origin = musicinfo.split(',')
        melody = process(origin)

        # 총 재생 시간 계산
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))

        playtime = (end_h - start_h) * 60 + end_m - start_m
        repeat = playtime // len(melody)
        remain = playtime % len(melody)

        # 전체 멜로디 문자열 만들기
        sound = process(melody) * repeat + melody[:remain]
        print(sound)

        # 기억하는 멜로디가 맞는지 확인
        if memory in sound:
            if not result or playtime > result[1]:
                result = (title, playtime)

    return result[0] if result else '(None)'
