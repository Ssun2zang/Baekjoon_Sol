def solution(s):
    pc = 0
    yc = 0
    for c in s:
        if c=="p"or c=="P":
            pc +=1
        elif c == "y"or c=="Y":
            yc +=1
    return pc==yc
    