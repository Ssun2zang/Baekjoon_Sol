from collections import deque
import sys
input = sys.stdin.readline
    
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
qList = deque()

for i in range(n):
    if A[i] == 0:
        qList.append(B[i])

M = int(input())
C = list(map(int, input().split()))

answer = []
for i in C:
    qList.appendleft(i)
    answer.append(qList.pop())

print(*answer)
