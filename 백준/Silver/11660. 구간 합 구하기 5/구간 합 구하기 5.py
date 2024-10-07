# N x N 이차원 배열 
# x1, y1 -> x2, y2까지 합 구하는 프로그램 작성 (1-N : 좌표)
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

array = []

for _ in range(N):
    array.append(list(map(int, input().split())))

tasks = []

for _ in range(M):
    tasks.append(list(map(int, input().split())))

subSum = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        subSum[i][j] = subSum[i-1][j] + subSum[i][j-1] + array[i-1][j-1] - subSum[i-1][j-1]

answers = []

for t in tasks:
    a, b, c, d = t
    answers.append(subSum[c][d] - subSum[c][b-1] - subSum[a-1][d] + subSum[a-1][b-1])


for a in answers:
    print(a)