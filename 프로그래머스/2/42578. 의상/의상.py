# 얼굴 / 상의 / 하의 / 겉옷으로 나뉨

# 같은 이름의 의상은 존재하지 않음

def solution(clothes):
    code = {}
    for c in clothes:
        if c[1] in code.keys():
            code[c[1]] += 1
        else:
            code[c[1]] = 1
    
    answer = 1
    for k in code.keys():
        answer *= (code[k] + 1)

    return answer - 1