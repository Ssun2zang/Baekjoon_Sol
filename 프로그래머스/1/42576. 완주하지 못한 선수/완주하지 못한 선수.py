# 단 한명의 선수만 완주하지 못함

# 동명이인 있을 수도 있음

def solution(participant, completion):
    goal = {}
    
    for p in participant:
        if p in goal.keys():
            goal[p] += 1
        else:
            goal[p] = 1
    
    for c in completion:
        goal[c] -= 1

    for k in goal.keys():
        if goal[k] != 0:
            return k