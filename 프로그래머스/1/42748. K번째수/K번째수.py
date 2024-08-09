# i 번째부터 j번째 포함으로 자르기

# 정렬

# k번째 (index로 k-1) 요소

def solution(array, commands):
    answer = []
    for c in commands:
        temp = array[c[0]-1:c[1]]
        temp.sort()
        answer.append(temp[c[2]-1])
    return answer