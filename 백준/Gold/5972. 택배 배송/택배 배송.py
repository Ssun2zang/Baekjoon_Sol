# 이전에 풀다 실패한 다익스트라 문제
# 최소 여물 구하기 (양방향 길)
# 출발은 1, 헛간은 N
# 둘 이상 길에 대해 예외 처리 필요

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edges = {i:{} for i in range(N+1)}

INF = 987654321

for _ in range(M):
    A, B, C = map(int, input().split())
    if edges[A].get(B, INF) > C:
        edges[A][B] = C
        edges[B][A] = C


def dijkstra(graph, s, N):
    cur_dist, cur_dest = 0, s
    from heapq import heappush, heappop
    h = []
    distances = [INF for _ in range(N+1)]
    heappush(h, (cur_dist, cur_dest))
    while(h):
        cur_dist, cur_dest = heappop(h)
        if distances[cur_dest] < cur_dist:
            continue

        for node in graph[cur_dest].keys():
            next_dist, next_dest = cur_dist + graph[cur_dest][node], node
            if next_dist < distances[next_dest]:
                heappush(h, (next_dist, next_dest))
                distances[next_dest] = next_dist
    
    return distances

print(dijkstra(edges, 1, N)[N])