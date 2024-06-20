from collections import deque
import sys

input=sys.stdin.readline

n = int(input())
cmd = {'push':0, 'pop':1, 'size':2, 'empty': 3, 'top':4}
_cmd = -1
val = -1
d = []
for i in range(n):
    _msg = input().split()
    if len(_msg) == 1:
        _cmd = cmd[_msg[0]]
    else:
        _cmd = cmd[_msg[0]]
        val = int(_msg[1])
    if (_cmd == 0):
        d.append(val)
    elif (_cmd == 1):
        if (not d):
            print(-1)
        else:
            print(d.pop())
    elif (_cmd == 2):
        print(len(d))
    elif (_cmd == 3):
        if (not d):
            print(1)
        else:
            print(0)
    elif (_cmd == 4):
        if (not d):
            print(-1)
        else:
            print(d[-1])