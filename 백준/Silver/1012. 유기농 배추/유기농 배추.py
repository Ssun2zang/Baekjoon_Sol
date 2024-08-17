# 배추 흰 지렁이가 있으면 인접한 배추로 이동함
# 한 배추의 상하좌우 네 방향이 보호 받을 수 있음

# 인접해있는 배추쌍을 찾으면 됨

T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

answers = []
for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[False for _ in range(M)] for _ in range(N)]
    answer = 0
    plants = []
    for i in range(K):
        a, b = map(int, input().split())
        plants.append((b, a))
        ground[b][a] = True
    
    # print(ground)

    from collections import deque

    for p in plants:
        q = deque()
        if(ground[p[0]][p[1]]):
            answer +=1
            q.append(p)
            ground[p[0]][p[1]] = False
            curr = p
            while(q):
                curr = q.popleft()
                for i in range(4):
                    if(curr[0]+dy[i]>=N or curr[0]+dy[i]<0 or curr[1]+dx[i]>=M or curr[1]+dx[i]<0):
                        continue
                    else:
                        if (ground[curr[0]+dy[i]][curr[1]+dx[i]]):
                            q.append((curr[0]+dy[i],curr[1]+dx[i]))
                            ground[curr[0]+dy[i]][curr[1]+dx[i]] = False
    answers.append(answer)

for a in answers:
    print(a)