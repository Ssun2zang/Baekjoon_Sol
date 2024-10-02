# 준서는 최대한 가치있게 배낭을 싸려함
# N개의 물건이 있음
# 각 물건의 무게는 W, 가치는 V
# 최대 무게는 K
from pprint import pprint
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
things = []

for i in range(N):
    w, v = map(int, input().split())
    things.append((v, w))

dp = [[0 for _ in range(N)]for _ in range(K+1)]

# pprint(things)

# 초기값 넣어주기 (첫 번째 물건)
for i in range(things[0][1], K+1):
    dp[i][0] = things[0][0]

# 그 다음 물건부터 비교
for j in range(1, N): # 물건
    for i in range(1, K+1): # 무게
        # 내 물건을 넣거나, 이전 방법이 더 높거나
        if things[j][1] > i :
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = max(dp[i][j-1], things[j][0]+dp[i-things[j][1]][j-1])

print(dp[K][N-1])