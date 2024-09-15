# 헛간의 개수 N
# 양방향 길 A B를 연결

# 1번에서 멀어질 수록 감소

# 1. 숨어야하는 헛간 번호 (가장 작은 헛간 번호), 2. 그 헛간까지 거리, 3. 같은 거리를 갖는 헛간의 개수 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

ways = {i:[] for i in range(N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    ways[a].append(b)
    ways[b].append(a)

# print(ways)

from collections import deque

INF = 987654321

visited = [INF for _ in range(N+1)]
visited[0] = -1
cur = 1
visited[cur] = 0
q = deque()
q.append(cur)

while(q):
    cur = q.popleft()
    for n in ways[cur]:
        if (visited[n] == INF):
            q.append(n)
            visited[n] = visited[cur] + 1

cnt = 0
max_val = -1
ans = -1

for i, v in enumerate(visited):
    if (v > max_val):
        ans = i
        max_val = v
        cnt = 1
    elif(v==max_val):
        cnt +=1


print(ans, max_val, cnt)