from bisect import bisect_left, bisect_right


def solution(info, query):
    # 조건 객체 생성
    language_list = ['cpp', 'java', 'python', '-']
    task_list = ['backend', 'frontend', '-']
    career_list = ['junior', 'senior', '-']
    soul_food_list = ['chicken', 'pizza', '-']

    mapper = {}

    for lang in language_list:
        for task in task_list:
            for career in career_list:
                for soul_food in soul_food_list:
                    mapper[(lang, task, career, soul_food)] = []

    # info 객체 변환
    for i in info:
        apply_info = i.split()
        for condition in mapper.keys():
            for i in range(4):
                if condition[i] == '-':
                    pass
                elif apply_info[i] != condition[i]:
                    break
            else:
                mapper[condition].append(int(apply_info[-1]))

    # mapper value 배열 정렬
    for arr in mapper.values():
        arr.sort()

    # 쿼리 수행
    answer = []
    for q in query:
        remove = {'and': None}
        query_list = [i for i in q.split() if i not in remove]
        score = int(query_list[-1])
        query_tuple = tuple(query_list[:4])

        scores = mapper[query_tuple]
        cnt = len(scores) - bisect_left(scores, score)
        answer.append(cnt)

    return answer