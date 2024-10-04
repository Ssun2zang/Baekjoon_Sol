# 핵심 개발은 끝
# 모든 건물을 짓는데 걸리는 최소 시간을 이용하여 근사
# 여러 건물을 동시에 지을 수 있음

# 종류 N개
# 걸리는 시간 + 건물을 짓기 위해 먼저 지어져야하는 번혹 주어짐
import sys
input = sys.stdin.readline

N = int(input())

# 건물 데이터 저장
A = [[]for _ in range(N+1)]

# 건물 생산 시간
build = [0]*(N+1)

# 진입 차수 리스트
dgr = [0]*(N+1)

# 정답 리스트
answer = [0]*(N+1)

for i in range(1, N+1):
    ins = list(map(int, input().split()))
    build[i] = ins[0]
    for j in range(1, len(ins)-1):
        A[ins[j]].append(i)
        dgr[i] += 1

from collections import deque

q = deque()

for i in range(1, N+1):
    if dgr[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    for n in A[cur]:
        dgr[n] -= 1
        # 걸리는 시간 업데이트하기
        answer[n] = max(answer[n], answer[cur]+build[cur])
        if dgr[n] == 0:
            q.append(n)

for i in range(1, N+1):
    print(answer[i]+build[i])