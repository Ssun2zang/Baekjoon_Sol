# 방향 그래프
# V, E가 주어짐 (1-V 번호)
# 시작 정점 K
# u -> v (가중치 w)
# u랑 v는 다르고, w는 10 이하 자연수
# 두 정점 사이 여러 간선이 존재할 수 있음

# i번 정점으로의 최단 경로 출력, 자신은 0, 경로 없으면 INF
import sys
input = sys.stdin.readline

V, E = map(int, input().split())

K = int(input())

INF = 987654321

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

from heapq import heappop, heappush

def dijkstra(s):
    q = []
    distances = [INF]*(V+1)
    distances[s] = 0
    heappush(q, (0, s))

    while q:
        cur_dist, cur_dest = heappop(q)
        
        if distances[cur_dest] < cur_dist:
            continue
            
        for n in graph[cur_dest]:
            next_dest = n[0]
            next_dist = n[1] + cur_dist
            if distances[next_dest] > next_dist:
                heappush(q, (next_dist, next_dest))
                distances[next_dest] = next_dist
    
    return distances

for d in dijkstra(K)[1:]:
    if d!=INF:
        print(d) 
    else:
        print("INF")