# 직각 삼각형이 맞다면 right
# 아니면 wrong
import sys
input = sys.stdin.readline


sig = 1

l = list(map(int, input().split()))
l.sort()
sig = l[0]

answers = []
while(sig):
    a, b, c = l
    if (c*c == a*a+b*b):
        answers.append("right")
    else:
        answers.append("wrong")
    l = list(map(int, input().split()))
    l.sort()
    sig = l[0]

for a in answers:
    print(a)