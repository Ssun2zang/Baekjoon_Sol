import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
num = pow(a, b, c)

print(num)