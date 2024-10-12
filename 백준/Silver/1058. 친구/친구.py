# 가장 유명한 사람 구하는 법 -> 각 사람의 2-친구를 구하기
# 2-친구 -> 두 사람이 친구 or A,B랑 친구인 C가 존재 
# 가장 유명한 사람의 2-친구의 수를 출력
 
import sys
input = sys.stdin.readline
 
N =  int(input())

INF = float('inf')
	
dist = [[INF for _ in range(N)] for _ in range(N)]

for i in range(N):
	f = input()
	for j in range(N):
		if f[j] == 'Y':
			dist[i][j] = 1

for k in range(N):
	dist[k][k] = 0
	for i in range(N):
		for j in range(N):
			dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
   
answer = 0
for i in range(N):
    temp = 0
    for j in range(N):
        if  0 < dist[i][j] <= 2:
            temp += 1
    answer = max(answer, temp)

print(answer)