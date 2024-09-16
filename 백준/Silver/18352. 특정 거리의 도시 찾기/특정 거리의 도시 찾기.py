# 1 - N 까지 M개의 단방향 도로 (모든 거리는 1)
# 최단 거리가 정확히 K인 도시의 번호를 오름차순으로 한줄씩 출력

# 하나도 존재하지 않으면 -1

# BFS / DIJKSTRA 

import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

roads = {i : [] for i in range(N+1)}

for _ in range(M):
    A, B = map(int, input().split())
    roads[A].append(B)

def dijkstra(roads, s):
    INF = 987654321
    distances = [INF for _ in range(N+1)]
    cur_dist, cur_dest = 0, s
    distances[cur_dest] = cur_dist

    from heapq import heappop, heappush

    h = []
    heappush(h,(cur_dist, cur_dest))
    while(h):
        cur_dist, cur_dest = heappop(h)

        if distances[cur_dest] < cur_dist:
            continue
            
        for next in roads[cur_dest]:
            next_dist, next_dest = cur_dist + 1, next
            if distances[next_dest] > next_dist:
                distances[next_dest] = next_dist
                heappush(h, (next_dist, next_dest))
    return distances

distances = dijkstra(roads, X)

# print(distances)

answers = []

for i, val in enumerate(distances):
    if val == K:
        answers.append(i)

if answers:
    for a in answers:
        print(a)
else:
    print(-1)