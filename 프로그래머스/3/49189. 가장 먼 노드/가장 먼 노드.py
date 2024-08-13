# n개의 노드가 존재함
# 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 함

# 가장 멀리 떨어진 노드는 최단 경로로 이동했을 때 간선의 개수가 가장 많은 노드이다

# 간선은 양방향이다

from collections import deque

def solution(n, edge):
    edges = {}
    for i in range(1, n+1):
        edges[i] = []

    for e in edge:
        edges[e[0]].append(e[1])
        edges[e[1]].append(e[0])
    
    cur = 1
    q = deque([1])

    INF = 987654321

    visited = [INF for _ in range(n+1)]
    visited[0] = -1
    visited[1] = 0

    answer = 0

    while(q):
        cur = q.popleft()
        # 종료 조건은? 

        for v in edges[cur]:
            # 방문 안 했으면
            if (visited[v]==INF):
                q.append(v)
                visited[v] = visited[cur] +1
    
    max_val = max(visited)


    for i, v in enumerate(visited):
        if max_val == v:
            answer += 1

    return answer