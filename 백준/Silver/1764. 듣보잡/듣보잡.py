# A, B 주어질 때, A and B 명단 하기
# 사전순으로 출력

import sys
input = sys.stdin.readline

listen = set()
see = set()

N, M = map(int, input().split())

for _ in range(N):
    listen.add(input())

for _ in range(M):
    see.add(input())

answers = list(listen&see)
answers.sort()

print(len(answers))

for a in answers:
    print(a, end="")