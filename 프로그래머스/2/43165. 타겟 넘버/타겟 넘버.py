# 음이 아닌 정수가 주어지고, 순서를 바꾸지 않고 더하거나 빼서 타겟 넘버를 만듦 

# dfs로 풀기 -> 지금까지 계산한 값을 저장함

# 성공 여부는 어떻게 저장하지? answer += 1 이걸 어케하죠?

# 2의 50승의 배열을 저장한다...? 

from collections import deque
def solution(numbers, target):
    q = deque([(0, 0)])
    answer = 0
    while (q):
        cv = q.popleft()
        if (cv[1]>=len(numbers)):
            if(cv[0]==target):
                answer +=1 
        else:
            q.append((cv[0] + numbers[cv[1]], cv[1]+1))
            q.append((cv[0] - numbers[cv[1]], cv[1]+1))

    return answer