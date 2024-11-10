import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

from itertools import permutations

perms = list(set(permutations(numbers, m)))

perms.sort(key = lambda x : tuple(x))

for perm in perms:
    for n in perm:
        print(n, end = " ")
    print("")