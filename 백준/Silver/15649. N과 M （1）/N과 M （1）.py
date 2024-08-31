from itertools import permutations;

N, M = map(int, input().split())

a = [i for i in range(1, N+1)]

perms = permutations(a, M)

for perm in perms:
    for i in range(M-1):
        print(perm[i], end=" ")
    print(perm[-1])
        