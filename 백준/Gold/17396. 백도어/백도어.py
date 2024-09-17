# 유섭이는 백도어를 한다
# 최대한 빨리 넥서스에 가고 싶다
# N개의 분기점에 위치 가능하다
# 0번째에 위치
# N-1은 상대 넥서스

# 모든 분기점을 갈 수 있는게 x -> 와드, 미니언, 포탑은 못 감
# 분기점 지나칠 수 있는지 여부와, 시간이 주어짐
# 연결은 양방향 (간선은 최대 하나)

# 못 가면 -1
# 최소 시간 출력하기

import sys
input = sys.stdin.readline

# N은 분기점 수, M은 간선 수
N, M = map(int, input().split())

# 시야 정보
light = list(map(int, input().split()))

INF = 9999987654321

# 거리 시간 정보
ways = {i:{} for i in range(N)}

# 나한테 가기
for i in range(N):
    ways[i][i] = 0

# 가기
for _ in range(M):
    a, b, t = map(int, input().split())
    ways[a][b] = t
    ways[b][a] = t

from heapq import heappop, heappush

def dijkstra(ways, s, N):
    distances = [INF]*N
    cur_dist, cur_dest = 0, s
    distances[cur_dest] = cur_dist
    h = []
    heappush(h, (cur_dist, cur_dest))

    while(h):
        cur_dist, cur_dest = heappop(h)

        if distances[cur_dest] < cur_dist:
            continue

        if cur_dest == N-1:
            return distances

        for i in ways[cur_dest]:
            if light[i] == 1 and i != N-1:
                continue
            next_dist, next_dest = cur_dist + ways[cur_dest][i], i
            if distances[next_dest] > next_dist:
                distances[next_dest] = next_dist
                heappush(h, (next_dist, next_dest))
    
    return distances

distances = dijkstra(ways, 0, N)
print(distances[N-1] if distances[N-1] != INF else -1)