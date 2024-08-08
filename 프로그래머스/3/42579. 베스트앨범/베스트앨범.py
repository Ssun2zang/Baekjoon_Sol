# 많이 재생된 장르 먼저 수록

# 장르 내에서 많이 재생된 노래 먼저 수록

# 재생 횟수가 같은 노래는 고유 번호 낮은 노래 먼저 수록

def solution(genres, plays): 
    songs = {}
    counts = {}

    for i in range(len(genres)):
        if genres[i] in songs.keys():
            songs[genres[i]].append((i, plays[i]))
            counts[genres[i]] += plays[i]
        else:
            songs[genres[i]] = [(i, plays[i])]
            counts[genres[i]] = plays[i]
    
    genre_count = []
    for k in counts.keys():
        genre_count.append((k, counts[k]))
    genre_count.sort(key=lambda x: x[1])

    answer = []

    for g in reversed(genre_count):
        temp = sorted(songs[g[0]], key=lambda x:(x[1], -x[0]))
        answer.append(temp[-1][0])
        if len(temp) > 1:
            answer.append(temp[-2][0])
    
    return answer