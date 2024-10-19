# 피보나치 계산 중 1과 0이 출력되는 횟수를 구하기...?

import sys
input = sys.stdin.readline

dp_0 = [0] * 41
dp_1 = [0] * 41

dp_0[0] = 1
dp_1[1] = 1

for i in range(2, 41):
    dp_0[i] = dp_0[i-1] + dp_0[i-2]
    dp_1[i] = dp_1[i-1] + dp_1[i-2]

T = int(input())

for _ in range(T):
    t = int(input())
    print(dp_0[t], end = " ")
    print(dp_1[t])