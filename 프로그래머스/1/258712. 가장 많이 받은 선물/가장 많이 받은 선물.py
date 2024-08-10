# 누가 선물을 많이 받을지 예측

# 두 사람이 주고 받으면, 이번 달까지 더 많이 준 사람이 다음달에 선물을 하나 받음

# 하나도 주고받지 않거나, 주고받은 수가 같으면 선물지수가 큰 사람이 하나 받음 (선물 지수가 같으면 주고 받지 않음)

# 선물 지수는 준 선물 - 받은 선물 (준 선물이 많은 사람이 받음)

# 가장 많이 받을 선물의 수

def solution(friends, gifts):
    # names = {}
    # for i in range(len(friends)):
    #     names[friends[i]]=i

    names = {friends[i]: i for i in range(len(friends))}

    records = [[0 for _ in range(len(friends))] for _ in range(len(friends))]

    for g in gifts:
        a, b = g.split()
        records[names[a]][names[b]] += 1

    scores = [0 for _ in range(len(friends))]

    for i in range(len(friends)):
        score = 0
        for j in range(len(friends)):
            score += records[i][j]
            score -= records[j][i]
        scores[i] = score
    

    next = [0 for _ in range(len(friends))]

    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            # 주고 받았으면
            if records[i][j] or records[j][i]:
                if records[i][j] > records[j][i]:
                    next[i] += 1
                elif records[i][j] < records[j][i]:
                    next[j] += 1
                else:
                    # 둘 다 같으면
                    # 선물 지수 비교 
                    if scores[i] > scores[j]:
                        next[i] += 1
                    elif scores[i] < scores[j]:
                        next[j] += 1
            # 안 주고 받았으면
            else:
                # 선물지수 비교
                if scores[i] > scores[j]:
                    next[i] += 1
                elif scores[i] < scores[j]:
                    next[j] += 1
    answer = max(next)
    return answer