# 숫자 카드는 정수 하나가 적혀져 있음
# N개의 카드를 가짐
# 정수 M개가 있을 때, 가지고 있는지 아닌지 판단

import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards.sort()


M = int(input())
cases = list(map(int, input().split()))

answers = []

def is_exist(target):
    start = 0
    end = len(cards)-1
    while (start <= end):
        mid = (start + end)//2
        if cards[mid] == target:
            return 1
        elif  cards[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for c in cases:
    answers.append(is_exist(c))

for a in answers:
    print(a, end= " ")