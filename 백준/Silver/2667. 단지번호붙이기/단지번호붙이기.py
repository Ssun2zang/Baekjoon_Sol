# 정사각 지도가 있음
# 1이면 집, 0은 집 없음

# DFS 렛츠 고

import sys
input = sys.stdin.readline

N = int(input())
apart = []

for _ in range(N):
    apart.append(list(int(c) for c in input().strip()))

visited = [[False for _ in range(N)] for _ in range(N)]

move = [(0,1), (1,0), (-1, 0), (0, -1)]

answers = []

# 일단 모든 곳을 탐색
for i in range(N):
    for j in range(N):
        cur = (i, j)

        # 이미 방문했으면
        if visited[cur[0]][cur[1]]:
            continue

        # 방문함
        visited[cur[0]][cur[1]] = True
        
        # 집이 있으면
        if apart[cur[0]][cur[1]]:
            # dfs 탐색 시작
            s = [cur]
            cnt = 1
            while(s):
                cur = s.pop()
                for m in move:
                    a, b = cur[0]+m[0], cur[1]+m[1] 

                    # valid 체크
                    if (a < 0 or a >= N or b < 0 or b >= N):
                        continue
                    
                    # 방문 체크 + 집 없는지
                    if (visited[a][b] or not apart[a][b]):
                        continue
                    
                    # 방문 안 했고 집 있으니까
                    cnt += 1
                    visited[a][b] = True
                    s.append((a,b))
            answers.append(cnt)

print(len(answers))
answers.sort()
for a in answers:
    print(a)
