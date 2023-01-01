def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append(1)
    n = len(participant)
    for i in range(n):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
        else:
            pass
    return answer