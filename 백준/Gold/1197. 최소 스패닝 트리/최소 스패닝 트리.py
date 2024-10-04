# 최소 신장 트리란?
# 모든 노드를 연결할 때 사용된 에지의 가중치 합을 최소로 하는 트리
# 사이클 x, 에지의 개수는 항상 N-1

# 노드의 개수 V
# 에지의 개수 E

# a, b, c -> c가 음수일 수도 있음

# 스패닝 트리는 에지를 기준으로, 가중치가 증가하도록 저장을 해야함
import sys
input = sys.stdin.readline

V, E = map(int, input().split())

q = []
parent = [i for i in range(V+1)]

from heapq import heappop, heappush
for _ in range(E):
    a, b, c = map(int, input().split())
    heappush(q, (c, a, b))

def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a!=b:
        parent[b] = a

useEdge = 0
answer = 0

while useEdge < V-1:
    w, a, b = heappop(q)
    if find(a) != find(b):
        answer += w
        union(a, b)
        useEdge += 1

print(answer)