import sys
input = sys.stdin.readline

N = int(input())

sizes= list(map(int, input().split()))

T, P = map(int, input().split())

a = 0
b = 0
c = 0

for size in sizes:
    a += size//T
    if (size%T != 0):
        a += 1

b = N//P
c = N%P

print(a)
print(b, c)