# begin -> target으로 변환하는 과정
# 한 번에 한 개의 알파벳만 바꾸기 가능
# words에 있는 단어로만 변환 가능

# 최소 몇 단계의 가정을 거쳐 변환 가능한지 return

# 최소 몇 단계니까 bfs 사용

# begin과 target은 같지 않음

# 변환할 수 없는 경우 0을 return 

from collections import deque

def solution(begin, target, words):
    answer = 0
    # words에 없는 경우
    if target not in words:
        return answer
    # 시작 단어부터 최대 50개만 방문함
    
    INF = 9876544321
    visited = {}
    for w in words:
        visited[w] = INF

    words.append(begin)
    visited[begin] = 0
    q = deque()
    q.append(begin)

    while(q):
        cur = q.popleft()
        
        # 종료 여부 처리

        if (cur == target):
            answer = visited[cur]

        # 가능한 이동 넣기 (방문 체크, canChange)
        # visited도 처리하기 

        for k in visited.keys():
            if (canChange(k, cur) and visited[k]== INF):
                q.append(k)
                visited[k]=visited[cur]+1
            
    return answer

def canChange(str1, str2):
    one_diff = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if not one_diff:
                one_diff = True
            else:
                return False
    return True