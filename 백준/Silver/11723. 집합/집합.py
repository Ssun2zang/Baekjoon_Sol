# 연산 수행 문제, check 시 결과 출력

import sys
input = sys.stdin.readline

S = set()
all_list = [str(i) for i in range(1, 21)]

M = int(input())
for _ in range(M):
    ins = input().split()
    cmd = ins[0]

    if cmd == 'add':
        S.add(ins[1])
    elif cmd == 'remove':
        if ins[1] in S:
            S.remove(ins[1])
    elif cmd == 'check':
        print(1 if ins[1] in S else 0)
    elif cmd == 'toggle':
        if ins[1] in S:
            S.remove(ins[1])
        else:
            S.add(ins[1])
    elif cmd == 'all':
        S = set(all_list)
    elif cmd == 'empty':
        S = set()
