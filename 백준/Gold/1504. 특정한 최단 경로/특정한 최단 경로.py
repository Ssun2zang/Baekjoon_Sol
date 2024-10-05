# 방향 없는 그래프 (양방향)
# 1- N번 정점 최단거리 이동 필요
# 조건 -> 최단 경로 + 임의로 주어진 두 정점을 반드시 통과

# 한 번 이동했던 정점과 이동했던 간선도 다시 이동 가능
# 최단 경로의 길이 출력하기

# 방법 1 -> v1 -> v2 -> N
# 방법 1-> v2 -> v1 -> N
import sys
input = sys.stdin.readline
N, E = map(int, input().split())

edges = [{} for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a][b] = c
    edges[b][a] = c

v1, v2 = map(int, input().split())

from heapq import heappop, heappush
INF = 987654321

def dijkstra(s):
    distances = [INF]*(N+1)

    distances[s] = 0
    h = []
    heappush(h, (0, s))
    while h:
        cur_dist, cur_dest = heappop(h)

        if cur_dist > distances[cur_dest]:
            continue
        
        for i in edges[cur_dest].keys():
            next_dist, next_dest = distances[cur_dest] + edges[cur_dest][i], i
            if distances[next_dest] > next_dist:
                distances[next_dest] = next_dist
                heappush(h, (next_dist, next_dest))
    
    return distances

fromStart = dijkstra(1)
fromV1 = dijkstra(v1)
fromV2 = dijkstra(v2)

answer = min(fromStart[v1]+fromV1[v2]+fromV2[N], fromStart[v2]+fromV2[v1]+fromV1[N])
print(answer if answer < INF else -1)