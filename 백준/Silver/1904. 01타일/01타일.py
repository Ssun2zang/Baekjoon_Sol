# 00과 1을 사용해서 총 길이가 N인 숫자를 만드는 가짓수 계산
# 2진 수열의 개수를 15746으로 나눈 나머지를 출력

# N개의 자리가 있는데 00의 자리를 고르는 가짓수와 같음. . .

# 수학 문제? 시간 제한이 짧음 -> 0.75초
# N은 100만 
# 최대 NlogN? or N?

# 알고리즘 -> DP

# 1일 때  -> 1
# 2일 때 00, 11 -> 2
# 3일 때 100, 001, 111 -> 3
# 4일 때, 1001, 0011, 1111, 0000, 1001 -> 5
# 5일 때, 00111, 10011, 11001, 11100, 00100, 00001, 10000, 11111 -> 8 
# 왜 합이지...?

import sys

input = sys.stdin.readline

N = int(input())

if (N ==1):
    print(1)
    exit()
elif( N==2):
    print(2)
    exit()

a = 1
b = 2

cur = 0
for _ in range(N-2):
    cur = ( a+b )% 15746
    a, b = b, cur

print(cur)