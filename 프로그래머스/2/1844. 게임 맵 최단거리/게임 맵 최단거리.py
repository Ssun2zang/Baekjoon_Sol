# nxm 맵에서 시작
# 1,1 -> n, m으로
# 0이 벽, 1이 길

# 도착하지 못한 경우에는 -1을 return

# 상대 팀 진영에 도착하기 위해 지나야 하는 칸의 개수의 최솟값

# 경로의 최솟값을 구해야하기 때문에??? bfs를 써야할 듯 함
# 만약 n, m에 도달하지 못한다면 -1을 return 하는 로직이 필요함
# 이동은 상하좌우로 할 거고, 1일 때만 움직일 수 있고 n, m 벗어나는지 인덱스가 음수인지 확인해야함
# 이미 방문한 곳을 다시 돌아올 이유가 없음

from collections import deque

INF = 987654321

def solution(maps):
    answer = -1
    move = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    n, m = len(maps), len(maps[0])
    visited = [[INF for _ in range(m)] for _ in range(n)]

    q = deque()

    q.append((0, 0))
    visited[0][0] = 0

    while(q):
        cur = q.popleft()
        if (cur[0] == n-1 and cur[1] == m-1):
            answer = visited[n-1][m-1]+1
        for mv in move:
            temp_n, temp_m = cur[0]+mv[0], cur[1]+mv[1]
            if (0<=temp_n<n and 0<=temp_m<m and maps[temp_n][temp_m] and visited[temp_n][temp_m]== INF):
                q.append((temp_n, temp_m))
                visited[temp_n][temp_m] = visited[cur[0]][cur[1]] + 1
    return answer
