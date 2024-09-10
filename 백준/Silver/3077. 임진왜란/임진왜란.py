# N(N-1)/2 조합을 모두 골라 올바른 순서면 1점
# 현우의 점수를 구하는 프로그램 작성하기
# 포맷은 (점수/총점)

N = int(input())

# 정답
wars = list(input().split())

# 현우가 쓴 답안
answers = list(input().split())

war_dict = {}
for i in range(N):
    war_dict[wars[i]] = i

from itertools import combinations

combs = list(combinations(answers, 2))

score = 0

for c in combs:
    if war_dict[c[0]] < war_dict[c[1]]:
        score += 1

print(str(score)+"/"+str(len(combs)))