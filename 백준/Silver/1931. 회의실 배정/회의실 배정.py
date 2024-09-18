# N개의 회의가 있음
# 시작과 끝나는 시간이 주어짐
# 끝나는 동시에 다음 회의 가능
# 시작시간과 끝나는 시간이 같을 수 있음

# 가능한 최대 회의 개수 구하기

# 끝나는 시각을 기준으로 그리디하면 될 것 같은데...

import sys
input = sys.stdin.readline

N = int(input())

meetings = []

for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key= lambda x: (x[1], x[0]))

answer = 1
cur = meetings[0][1]

for i, meeting in enumerate(meetings[1:]):
    if meeting[0] >= cur:
        answer +=1
        cur = meeting[1]

print(answer)