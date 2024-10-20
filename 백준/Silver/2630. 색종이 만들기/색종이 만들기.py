# 1과 0으로 만들어진 색종이
# 각 색을 정사각형으로 자르려고 함 (전체의 반으로만 자름)
# 각 색의 정사각형 수를 출력하기

import sys
input = sys.stdin.readline

N = int(input())

paper = []

for _ in range(N):
    paper.append(list(map(int, input().split())))
    
    
answer = [0, 0]

def is_one_color(x, y, size):
    if size == 1:
        answer[paper[x][y]] += 1
        return 
    
    color = paper[x][y]
    for i in range(size):
        for j in range(size):
            if color != paper[x+i][y+j]:
                is_one_color(x, y, size//2)
                is_one_color(x + size//2, y, size//2)
                is_one_color(x, y + size//2, size//2)
                is_one_color(x + size//2, y + size//2, size//2)
                return
    answer[color] += 1
    return

is_one_color(0,0, N)

for a in answer:
    print(a)