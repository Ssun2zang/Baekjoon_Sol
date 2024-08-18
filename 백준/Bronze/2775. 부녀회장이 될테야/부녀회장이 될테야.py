# a층 b호에 살려면, (a-1)층 부터 b호까지 사람의 수의 합을 데려와야 함
# k층에 n호에 몇명이 사는지 출력하기
# 0층 부터 있고, 1호부터 - i호에는 i명을 삽니다


T = int(input())

dp = [[0 for _ in range(15)] for _ in range(15)]

# dp는 초기값을 정해주고 돌려야함
for i in range(15):
    dp[0][i] = i

# 점화식을 정해야함
for i in range(1, 15):
    for j in range(1, 15):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

# print(dp)

for t in range(T):
    K = int(input())
    N = int(input())

    print(dp[K][N])