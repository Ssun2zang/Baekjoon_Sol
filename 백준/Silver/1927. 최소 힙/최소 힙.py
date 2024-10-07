# 최소 힙
# x 넣기
# 가장 작은 값 출력 후 제거

import sys
input = sys.stdin.readline
from heapq import heappop, heappush

h = []

answers = []

N = int(input())

for _ in range(N):
    t = int(input())
    if t == 0:
        if h:
            answers.append(heappop(h))
        else:
            answers.append(0)
    else:
        heappush(h, t)

for a in answers:
    print(a)