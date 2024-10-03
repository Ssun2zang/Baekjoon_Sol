# N과 M 사이의 소수를 구하기
# 에라토스테네스의 체로 소수를 구해야함
# N까지의 수에서, 1~N의 제곱근의 배수를 소거하며 풀기
import sys
from math import sqrt
input = sys.stdin.readline


M, N = map(int, input().split())

arr = [True for i in range(N+1)]

arr[0] = False
arr[1] = False

for i in range(2, int(sqrt(N))+1):
    # 이미 컷당함
    if not arr[i]:
        continue
    for j in range(2*i, N+1, i):
        arr[j] = False

for i in range(M, N+1):
    if arr[i]:
        print(i)