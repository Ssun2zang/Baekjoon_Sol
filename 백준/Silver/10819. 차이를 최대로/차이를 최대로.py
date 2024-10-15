# 배열에 들어있는 정수의 순서를 바꿔서 식의 최댓값을 구하기
# 순열로 일일이 계산하기

import sys
input = sys.stdin.readline

from itertools import permutations

N = int(input())

nums = list(map(int, input().split()))

answer = 0

for p in permutations(nums):
    temp = 0
    for i in range(N-1):
        temp += abs(p[i]-p[i+1])
    answer = max(answer, temp)

print(answer)