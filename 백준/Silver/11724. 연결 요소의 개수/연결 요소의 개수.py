# 방향 없는 그래프에서 연결 요소의 수를 구하는 프로그램
# 정점 N개, 간선 M개

# 연결 요소의 개수 구하기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

from collections import deque

visited = [False] * (N+1)

edges = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

answer = 0

for i in range(1, N+1):
    q = deque()
    if visited[i]:
        continue
    else:
        answer += 1
        q.append(i)
        visited[i] = True
        while q:
            cur = q.popleft()
            for n in edges[cur]:
                if not visited[n]:
                    q.append(n)
                    visited[n] = True

print(answer)