# 두 플레이어가 차례로 돌아가면서 진행
# 선 -> 홀수
# 후 -> 짝수
# 0 - n-1까지 고유 번호가 부여된 평면 상의 점 n개 -> 일직선 x
# 두 점 선택 선분 그음
# 사이클이 생기면 종료
# 한 끝점에서 출발해서 출발점으로 되돌아오기

# 몇 번째 차례에 사이클이 생기는지 출력하기

# 딱... 유니온 파인드 문제
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

parents = [i for i in range(n+1)]

def find(a):
    if parents[a] == a:
        return a
    else:
        parents[a] = find(parents[a])
        return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parents[b] = a

def isSameSet(a, b):
    a = find(a)
    b = find(b)
    return a == b

answer = 0 
for i in range(m):
    a, b = map(int, input().split())
    if isSameSet(a, b):
        answer = i+1
        break
    union(a, b)

print(answer)
