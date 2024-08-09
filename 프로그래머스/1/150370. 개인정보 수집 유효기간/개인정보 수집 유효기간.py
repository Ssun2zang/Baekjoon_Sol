# 1 ~ n 개의 약관이 존재

# 개인정보는 유효기간 전까지만 보관 가능

# 모든 달을 28일까지 있다고 가정함

# 파기해야할 개인정보의 번호를 오름차순으로 return

def solution(today, terms, privacies):
    answer = []
    rules = {}
    
    ty, tm, td = map(int, today.split("."))

    for t in terms:
        a, b = t.split()
        rules[a] = b
    
    for index, p in enumerate(privacies):
        date, rule = p.split()
        y, m, d = map(int, date.split("."))
        if getTimeValue(ty, tm, td) >= getTimeValue(y, m+int(rules[rule]), d):
            answer.append(index+1)

    return sorted(answer)

def getTimeValue(y, m, d):
    return (y-2000)*28*12 + m*28 + d