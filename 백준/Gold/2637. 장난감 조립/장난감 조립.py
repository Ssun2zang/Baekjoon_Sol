# 기본 부품 + 중간 부품 사용해서 조립
# 기본 부품은 조립될 수 없고
# 중간 부품은 중간 + 기본으로

# 완제품이랑 필요한 부품 사이 관계 -> 완제품으로 조립하기 위해 필요한 기본 부품의 종류 개수

# 각 줄에 부품 번호가 작은 것보다 큰 순서가 되게 부품 번호 + 소요 개수 출력

import sys
input = sys.stdin.readline

# 완제품 번호
N = int(input())

# 부품 관계 개수
M = int(input())

degrees = [0]*(N+1)
makes = [[] for _ in range(N+1)]

for _ in range(M):
    x, y, k = map(int, input().split())
    degrees[x] += 1
    makes[y].append((x, k))

answer = [[0 for _ in range(N+1)]for _ in range(N+1)]

from collections import deque

q = deque()

defaults = []

# 기본 부품들
for i in range(1, N+1):
    if degrees[i] == 0:
        answer[i][i] = 1
        q.append(i)
        defaults.append(i)

while q:
    cur = q.popleft()
    for make in makes[cur]:
        x, k = make
        degrees[x] -= 1
        for i, a in enumerate(answer[cur]):
            if a == 0:
                continue
            answer[x][i] += a * k
        if degrees[x] == 0:
            q.append(x)

for d in defaults:
    print(d, answer[N][d])
        