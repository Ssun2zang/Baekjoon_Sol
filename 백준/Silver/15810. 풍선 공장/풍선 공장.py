# N 명의 스태프
# M개의 풍선을 만들것
# 풍선 하나 만들 때 A_i

# 최소 시간 출력하기

N, M = map(int, input().split())
A = list(map(int, input().split()))

start = 0
end = max(A) * M
mid = (start+end)//2
answer = end

while (start <= end):
    temp = M
    is_answer = False
    for i in range(N):
        temp -= mid//A[i]
        if (temp <= 0):
            is_answer = True
            break
    if (is_answer):
        answer = mid
        end = mid - 1
        mid = (start+end)//2
    else:
        start = mid + 1
        mid = (start+end)//2

print(answer)