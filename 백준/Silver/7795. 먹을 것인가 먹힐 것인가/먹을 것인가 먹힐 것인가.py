# 심해에 A-> B를 먹음
# A는 자기보다 작은 먹이만 먹을 수 있음

# 두 생명체 A, B가 주어질 때 A가 B보다 큰 쌍의 개수 구하기

# 오후에 다시해보자!

import sys
input = sys.stdin.readline

T = int(input())

answers = []

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    INF = 9876543221

    A.sort()
    B.sort()
    B.append(INF)

    ai = 0
    bi = 0
    answer = 0

    while (ai < N):
        # bi 이동 로직
        if (A[ai] > B[bi] and bi <= M):
            bi += 1
        else:
            ai += 1
            answer += bi

    answers.append(answer)

for a in answers:
    print(a)