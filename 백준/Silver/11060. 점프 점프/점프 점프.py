# 1xN 크기의 미로
# 각 칸에 정수가 쓰여져 있고, 
# 적힌 정수 이하만큼 떨어진 칸에 점프할 수 있음 (오른쪽으로)

# 최소 몇 번 점프해야하는지
# 못 갈 경우 -1 출력

import sys
input = sys.stdin.readline

N = int(input())

maze = list(map(int, input().split()))

from collections import deque

cur = 0
INF = 987654321
visited = [INF] * N
visited[cur]=0

q = deque()
q.append(cur)

while(q):
    cur = q.popleft()
    for i in range(1, maze[cur]+1):
        if cur + i >= N:
            continue

        if visited[cur+i] > visited[cur] + 1:
            visited[cur+i] = visited[cur] + 1
            q.append(cur+i)


print(visited[N-1] if visited[N-1]!= INF else -1)