# 바이러스 확산을 막으려고 벽을 세울 것

# NxM 직사각형, 1x1 정사각형으로 나뉨
# 연구소는 빈칸 + 벽

# 상하좌우 인접한 빈 칸으로 퍼짐
# 세로 세울 벽의 개수는 꼭 3개

# 0은 빈 칸, 1은 벽, 2는 바이러스
# 안전 영역의 최댓값을 구하기

N, M = map(int, input().split())

rooms = []

for _ in range(N):
    rooms.append(list(map(int, input().split())))

empty = []
virus = []

for i, rows in enumerate(rooms):
    for j in range(M):
        if rows[j] == 0:
            empty.append((i, j))
        elif rows[j] == 2:
            virus.append((i, j))

from itertools import combinations

wall_combs = combinations(empty, 3)

max_val = 0

from collections import deque

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for wall_comb in wall_combs:
    visited = [[False for _ in range(M)] for _ in range(N)]
    cur_val = len(empty) - 3
    for w in wall_comb:
        visited[w[0]][w[1]] = True

    for v in virus:
        cur = v
        q = deque()
        visited[cur[0]][cur[1]] = True
        q.append(v)
        while(q):
            cur = q.popleft()
            for m in move:
                a, b = cur[0]+ m[0], cur[1]+m[1]
                if (0<=a<N and 0<=b<M):
                    if(not visited[a][b] and rooms[a][b] == 0):
                        q.append((a,b))
                        visited[a][b] = True
                        cur_val -= 1
    
    if (cur_val > max_val):
        max_val = cur_val

print(max_val)