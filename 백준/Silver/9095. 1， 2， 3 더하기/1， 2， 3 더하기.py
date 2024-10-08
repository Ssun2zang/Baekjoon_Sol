# 1, 2, 3의 합으로 숫자 나타내기
import sys
input = sys.stdin.readline

dp = [0]*11

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

T = int(input())
answers = []
for i in range(T):
    t = int(input())
    answers.append(dp[t])

for a in answers:
    print(a)