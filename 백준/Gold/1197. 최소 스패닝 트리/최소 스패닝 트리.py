import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v, e = map(int, input().split())

from heapq import heappop, heappush

h = []

for i in range(e):
    a, b, c = map(int, input().split())
    heappush(h, (c, a, b))

parent = [i for i in range(v+1)]

def find(a):
    if parent[a]==a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a
    
answer = 0

cnt = v-1

while(cnt):
    w, s, e = heappop(h)
    if (find(s) != find(e)):
        union(s, e)
        cnt -= 1
        answer += w

print(answer)