import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = []
for i in range(N):
    nums.append(i+1)

from itertools import combinations

combs = combinations(nums, M)

for comb in combs:
    for n in comb:
         print(n, end = " ")
    print("")