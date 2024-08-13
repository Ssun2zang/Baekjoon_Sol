# 구명보트로 사람을 구출
# 최대 2명, 무게 제한이 있음

# 구명보트를 최대한 적게 써서 모든 사람 구출하려 함
# 무게 제한은 항상 몸무게 중 최댓값보다 큼

from collections import deque

def solution(people, limit):
    people.sort()
    answer = 0

    q = deque(people)

    while(q):
        answer +=1
        if (len(q)==1):
            break
        if (q.pop() + q[0] <= limit):
            q.popleft()
    
    return answer