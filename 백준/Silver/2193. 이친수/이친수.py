# 0과 1로만 이루어진 수
# 이친수는 0으로 시작 x
# 1이 두번 연속 나오지 않음
# dp

# n-1에 0으로 끝나는 거 -> 1, 0
# n-1에 1로 끝나는 거 -> 0

import sys
input = sys.stdin.readline

N = int(input())

dp = [(0,0)]*(N+1)

dp[1] = (0, 1)

for i in range(2, N+1):
    dp[i]= (dp[i-1][0]+dp[i-1][1], dp[i-1][0])

print(dp[N][0] + dp[N][1])