import sys
input = sys.stdin.readline

N = int(input())

from heapq import heappop, heappush

h = []
answers = []

for _ in range(N):
    num = int(input())
    if num == 0:
        if h:
            print(-heappop(h))
        else:
            print(0)
    else:
        heappush(h, -num)