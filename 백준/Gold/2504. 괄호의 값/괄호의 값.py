import sys

input = sys.stdin.readline

def checkString(str):
    stack = []
    value = [[]]
    for c in str[:-1]:
        if (c == ')'):
            if (not stack):
                print(0)
                return
            if (stack.pop() == '('):
                innerVal = value.pop()
                temp =2*max(1, sum(innerVal))
                value[-1].append(temp)
            else:
                print(0)
                return
        elif (c == ']'):
            if (not stack):
                print(0)
                return
            if (stack.pop() == '['):
                innerVal = value.pop()
                temp =3*max(1, sum(innerVal))
                value[-1].append(temp)
            else:
                print(0)
                return
        else:
            stack.append(c)
            value.append([])
    if (len(stack)==0):
        print(sum(value[0]))
    else:
        print(0)


str = input()
checkString(str)