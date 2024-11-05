import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [i+1 for i in range(N)]

from itertools import combinations_with_replacement

combs = combinations_with_replacement(nums, M)

for comb in combs:
    for num in comb:
        print(num, end = " ")
    print("")