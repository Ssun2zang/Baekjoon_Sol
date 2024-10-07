# 1 - N까지 번호가 있고, i번 사람이 인출하는 데 Pi분이 걸림
# 줄 서는 순서에 따라 필요하느 시간의 합이 달라짐
# 각 사람이 돈을 인출하는데 필요한 시간의 합

import sys
input = sys.stdin.readline

N = int(input())
persons = list(map(int, input().split()))
persons.sort()

answer = 0
prev = 0

for p in persons:
    answer += p + prev
    prev = p + prev

print(answer)