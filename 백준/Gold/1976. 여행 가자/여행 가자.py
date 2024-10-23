# 가능한 여행인지 (여행지가 다 같은 집합인지 확인하기)
import sys
input =sys.stdin.readline

N = int(input())
M = int(input())

parents = [i for i in range(N+1)]

def find(a):
    if parents[a] == a:
        return a
    else:
        parents[a] = find(parents[a])
        return parents[a]
    
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parents[b] = a
        
for i in range(1, N+1):
    cities = list(map(int, input().split()))
    for j in range(N):
        if cities[j]:
            if find(i) != find(j+1):
                union(i, j+1)

want = list(map(int, input().split()))

temp = find(want[0])
answer = "YES"
for w in want[1:]:
    if find(w) != temp:
        answer = "NO"
        break
    
print(answer)