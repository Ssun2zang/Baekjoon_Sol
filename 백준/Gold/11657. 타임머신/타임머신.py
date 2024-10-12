# N개의 도시
# 한 도시에서 다른 도시에 도착하는 버스 M개
# A, B, C 시작, 도착, 이동 시간
# C가 음수일 수도
# 1번 도시에서 출발해, 2 ~ N번 도시로 가는 빠른 시간을 순서대로 출력 (경로가 없다면 -1)
# 무한히 오래전으로 돌릴 수 있다면, 첫째 줄에 -1 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []

INF = float('inf')
for i in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

def bellman_ford(s):
    dists = [INF]*(N+1)
    dists[s] = 0
    for i in range(N): 
        for cur, next, v in edges:
            next_dist = dists[cur] + v
            if dists[cur] != INF and dists[next] > next_dist:
                dists[next] = next_dist
                if i == N-1:
                    return -1
    return dists

res = bellman_ford(1)
if res == -1:
    print(res)
else:
    for r in res[2:]:
        print(r if r != INF else -1)