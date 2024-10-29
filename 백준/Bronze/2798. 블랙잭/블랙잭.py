import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

from itertools import combinations

sets = combinations(cards, 3)

answer = -1

for s in sets:
    temp = sum(s)
    if temp > answer and temp <= M:
        answer = temp

print(answer)