import sys
input = sys.stdin.readline

M = int(input())

find = False

for num in range(1, M):
    temp = num
    nums = list(str(num))
    for n in nums:
        temp += int(n)
    if temp == M:
        print(num)
        find = True
        break

if not find:
    print(0)