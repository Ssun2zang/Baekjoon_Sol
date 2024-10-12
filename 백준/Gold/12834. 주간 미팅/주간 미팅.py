# KIST, 씨알푸드에서 함께 의논 작업
# 집-KSIT + 집-씨알
# 각 장소는 노드
# 도달 못하면 최단 거리는 -1
# 거리의 합

import sys
input = sys.stdin.readline

N, V, E = map(int, input().split())
A, B = map(int, input().split())
houses = list(map(int, input().split()))

INF = float('inf')
graph = [{} for _ in range(V+1)]

for i in range(E):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l    

from heapq import heappop, heappush

def dijkstra(s):
    dist = [INF]*(V+1)
    dist[s] = 0
    h = []
    heappush(h, (0, s))
    while h:
        cur_dist, cur_dest = heappop(h)
        
        if cur_dist > dist[cur_dest]:
            continue
        
        for k in graph[cur_dest].keys():
            next_dist, next_dest = cur_dist + graph[cur_dest][k], k
            if dist[next_dest] > next_dist:
                dist[next_dest] = next_dist
                heappush(h, (next_dist, next_dest))
    return dist

kistDist = dijkstra(A)
ssialDist = dijkstra(B)

answer = 0

for h in houses:
    if kistDist[h] != INF:
        answer += kistDist[h]
    else:
        answer -= 1
    if ssialDist[h] != INF:
        answer += ssialDist[h]
    else:
        answer -= 1

print(answer)