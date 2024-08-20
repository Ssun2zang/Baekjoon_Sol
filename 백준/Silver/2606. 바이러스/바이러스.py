# 연결되어 있으면 바이러스에 걸림
# 연결 정보를 통해 걸린 컴퓨터 수를 출력

N = int(input())
M = int(input())

conn = {i:[] for i in range(N+1)}
visited = [0 for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    conn[a].append(b)
    conn[b].append(a)

from collections import deque

q = deque()

q.append(1)
cur = 1
visited[1] = 1

while(q):
    cur = q.popleft()
    for n in conn[cur]:
        if visited[n] == 0:
            q.append(n)
            visited[n] = 1

print(sum(visited)-1)