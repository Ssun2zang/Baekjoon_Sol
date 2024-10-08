# 모든 지점에 대해 목표지점까지의 거리를 구하기
# 가로, 세로로만 움직일 수 있음

# n(세로), m(가로)
# 0은 갈 수 없음, 1은 갈 수 있고, 2는 목표 (2는 단 한개)
# 원래 갈 수 없는 땅인 위치는 0, 도달 못하면 -1

import sys
input = sys.stdin.readline

maze = []

N, M = map(int, input().split())

start = [0, 0]

for i in range(N):
    temp = list(map(int, input().split()))
    maze.append(temp)
    if 2 in temp:
        start = [i, temp.index(2)]

from collections import deque

visited = [[-1 for _ in range(M)] for _ in range(N)]
q = deque()
visited[start[0]][start[1]] = 0
q.append(start)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if maze[i][j] == 0:
            visited[i][j] = 0

while q:
    cur = q.popleft()
    for i in range(4):
        x, y = cur[0] + dx[i], cur[1] + dy[i]
        if not(x >= 0 and x < N and y >=0 and y < M):
            continue
        if visited[x][y] != -1 or visited[x][y] == 0 :
            continue
        else:
            visited[x][y] = visited[cur[0]][cur[1]] + 1
            q.append([x, y])

for row in visited:
    for r in row:
        print(r, end=" ")
    print()