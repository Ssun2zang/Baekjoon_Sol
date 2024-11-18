import sys
input = sys.stdin.readline

x = int(input())
y = int(input())
z = int(input())

num = x*y*z
num = list(str(num))

num_list = [0 for _ in range(10)]

for n in num:
    num_list[int(n)] += 1

for i in num_list:
    print(i)