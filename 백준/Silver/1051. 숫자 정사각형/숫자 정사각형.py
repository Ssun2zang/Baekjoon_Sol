# NxM 직사각형
# 각 칸에 한 자리 숫자가 적힘
# 꼭짓점에 쓰여있는 수가 모두 같은 가장 큰 정사각형 찾기

# 정사각형의 크기 출력하기
# 최소 1 -> n제곱

# N = 50, 대충 N 3제곱


N, M = map(int, input().split())

rec = []

for i in range(N):
        rec.append(list(map(int, list(input()))))

answer = 1

for i in range(N):
    for j in range(M):
        cur = rec[i][j]
        k = 1
        a = i + k
        b = j + k
        while(a<N and b<M):
            if(cur == rec[i][b] == rec[a][j] == rec[a][b]):
                answer = max(answer, (k+1)*(k+1))
            k += 1
            a += 1
            b += 1

print(answer)