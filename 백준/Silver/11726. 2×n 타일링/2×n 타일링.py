# 2*n 크기의 직사각형을 채우는 방법의 수 구하기

N = int(input())

# 1->1, 2->2, 3->3, 4-> 뒤에 | 하나 붙이기 + = 하나 붙이기
# n = n-1 + n-2

answer = 0


def findAnswer(N):

    a = 1
    b = 2

    if N == 1:  
        return a
    elif N == 2:
        return b
    
    answer = 0
    for _ in range(3, N+1):
        answer = (a + b)%10007
        a = b
        b = answer
    return answer

print(findAnswer(N))