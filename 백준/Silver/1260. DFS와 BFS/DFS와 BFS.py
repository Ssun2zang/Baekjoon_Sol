# DFS 탐색 결과와 BFS 탐색 결과를 출력
# 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것부터 방문
# 정점 번호 : 1 ~ N
# 양방향 간선

import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

for i in range(1, N+1):
    edges[i].sort()

visited = [False]*(N+1)

def dfs(s):
    print(s, end= " ")
    visited[s] = True
    for n in edges[s]:
        if not visited[n]:
            dfs(n)

dfs(V)

from collections import deque

def bfs(s):
    visited = [False]* (N+1)
    visited[s] = True
    q = deque()
    q.append(s)
    while(q):
        cur = q.popleft()
        print(cur, end=" ")
        for n in edges[cur]:
            if not visited[n]:
                q.append(n)
                visited[n] = True

print()
bfs(V)