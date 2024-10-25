import sys
input = sys.stdin.readline

N, M = map(int, input().split())

sites = {}

for _ in range(N):
    site, pwrd = input().split()
    sites[site] = pwrd
answers = []
for _ in range(M):
    s = input().strip()
    answers.append(sites[s])

for a in answers:
    print(a)