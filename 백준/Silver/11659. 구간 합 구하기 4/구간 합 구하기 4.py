# 구간합 구하기
# N: 수의 개수, 합을 구해야하는 횟수 M

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))

sums = [0]*(N+1)

for i in range(1, N+1):
    sums[i] = sums[i-1] + nums[i-1]

answers = []
for _ in range(M):
    i, j = map(int, input().split())
    answers.append(sums[j]-sums[i-1])

for answer in answers:
    print(answer)