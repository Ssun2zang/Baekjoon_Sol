# 학생들 줄 세우기
# 두 학생을 비교한 값만 있음
# 답이 여러가지면 아무거나 출력

# 1 < N < 32000
# 위상정렬 문제

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

degrees = [0]*(N+1)
orders = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    degrees[B] += 1
    orders[A].append(B)
    
from collections import deque

q = deque()

for i in range(1, len(degrees)):
    if degrees[i] == 0:
        q.append(i)

answer = []

while q:
    cur = q.popleft()
    answer.append(cur)
    for n in orders[cur]:
        degrees[n] -= 1
        if degrees[n] == 0:
            q.append(n)

for a in answer:
    print(a, end=" ")