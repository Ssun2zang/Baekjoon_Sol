# 모든 음식의 스코빌 지수를 올리기 위해 낮은 두 개를 섞음

# 점수 = 가장 낮은 + 두번째로 낮은 * 2

# 섞어야하는 최소 횟수를 담아 return하기

# 섞은 음식을 다시 넣어야하니까, 정렬을 빠르게 할 수 있는 heapq를 쓰는게 맞음

# 만들 수 없는 경우에는 -1을 return

from heapq import heapify, heappop, heappush

def solution(scoville, K):
    answer = 0
    heapify(scoville)

    while (scoville[0]<K):
        if (len(scoville) == 1):
            return -1
        a = heappop(scoville)
        b = heappop(scoville)
        
        heappush(scoville, a+2*b)
        answer += 1

    return answer