# 2원과 5원으로만 거슬러줘야함
# 동전 개수 최소가 되게 하기
# 거슬러 줄 수 없으면 -1

import sys
input = sys.stdin.readline

N = int(input())

answer = 0
answer += N//5

if (N%5)%2 == 0:
    answer += (N%5)//2
else:
    if answer >= 1:
        answer += (N%5 + 5)//2 - 1
    else:
        answer = -1

print(answer)