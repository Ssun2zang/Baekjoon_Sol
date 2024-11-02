import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    k = b - a
    answer = 0
    holder = 0
    while(k>0):
        answer +=1
        holder += (answer%2)
        k -= holder
    print(answer)