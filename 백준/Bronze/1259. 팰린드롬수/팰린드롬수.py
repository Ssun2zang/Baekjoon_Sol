import sys
input = sys.stdin.readline
answers = []

while (True) :
    num = int(input())
    if num == 0:
        break
    num = str(num)
    flag = False
    for i in range(len(num)//2):
        
        if num[i] != num[-i-1]:
            answers.append("no")
            flag = True
            break
    if not flag:
        answers.append("yes")

for a in answers:
    print(a)