# x가 3으로 나누어 떨어지면 3으로 나눔
# x가 2로 나누어 떨어지면 2로 나눔
# 1을 뺌

N = int(input())

dp = [0] * max((N+1), 4)
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, N+1):
    temp = []
    if i % 3 == 0:
        temp.append(dp[i//3] + 1)
    if i % 2 == 0:
        temp.append(dp[i//2]+1)
    temp.append(dp[i-1]+1)
    dp[i] = min(temp)

print(dp[N])