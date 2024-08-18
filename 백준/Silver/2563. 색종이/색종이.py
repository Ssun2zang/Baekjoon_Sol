# 가로, 세로가 100인 정사각형 도화지
# 가로, 세로 크기가 10인 정사각형 모양의 색종이를 평행하게 붙임
# 색종이가 붙은 영역의 넓이 구하기
# 색종이가 도화지 밖으로 나가는 경우는 없음

N = int(input())

paper = [[False for _ in range(100)] for _ in range(100)]

answer = 0

for  i in range(N):
    a, b = map(int, input().split())
    for j in range(10):
        for k in range(10):
            if paper[b+j][a+k] == False:
                answer += 1
                paper[b+j][a+k] = True

print(answer)
