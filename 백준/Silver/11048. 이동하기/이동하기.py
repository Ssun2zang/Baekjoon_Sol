# N x M 미로에 갇힘
# 가장 왼쪽 윗 방은 (1,1), 오른쪽 아랫방은 (N,M)

# 한 칸씩 이동 가능 (1, 0) (0, 1) (1, 1)
# 사방 다 가져갈 수 있음

# 가져올 수 있는 사탕 개수 최댓값
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dp = []

for i in range(N):
    dp.append(list(map(int, input().split())))

for i in range(1, N):
    dp[i][0] += dp[i-1][0]

for i in range(1, M):
    dp[0][i] += dp[0][i-1]


for i in range(1, N):
    for j in range(1, M):
        dp[i][j] += max(dp[i-1][j], dp[i][j-1])
print(dp[N-1][M-1])