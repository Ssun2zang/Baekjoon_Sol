# 도연이는 친구가 없다

# N x M 크기 캠퍼스에서 벽이 아닌 상하좌우로 이동하기, 만날 수 있는 사람의 수 출력

# O는 빈공간, X는 벽, I는 도연이, P는 사람이다

# 아무도 못 만나면 TT

N, M = map(int, input().split())

visited = [[False for _ in range(M)] for _ in range(N)]
school = []

for _ in range(N):
    school.append(list(input()))

# I 찾기

def findI(arr):
    for i, row in enumerate(school):
        if 'I' in row:
            return (i, row.index('I'))
    return None

I = findI(school)


moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def isValid(a, b, N, M, school):
    if (a >= N or a < 0 or b >= M or b < 0):
        return False
    if (school[a][b] == 'X'):
        return False
    return True

from collections import deque

q = deque()
q.append(I)
visited[I[0]][I[1]] = True

friends = 0

while(q):
    cur = q.popleft()
    for m in moves:
        a, b = cur[0]+m[0], cur[1]+m[1]
        if isValid(a, b, N, M, school):
            if (visited[a][b]):
                continue
            visited[a][b] = True
            q.append((a,b))
            if school[a][b] == 'P':
                friends +=1

print(friends if friends else "TT")