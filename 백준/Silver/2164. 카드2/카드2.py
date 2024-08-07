from collections import deque

dq = deque()
n = int(input())

for i in range(n):
    dq.append(i+1)

for j in range(n-1):
    dq.popleft()
    temp = dq.popleft()
    dq.append(temp)

print(dq.pop())