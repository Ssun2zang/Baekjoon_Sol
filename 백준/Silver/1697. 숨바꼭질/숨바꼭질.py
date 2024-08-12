# 수빈이는 N에 있음
# 동생은 K에 있음
# 수빈이는 걷거나 순가이동
# 걷기 : X -> X-1 or -> X+1
# 순간이동 : X -> 2*X

# 수빈이가 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하기

n, k = map(int, input().split())

answer = 0

found = False

from collections import deque

INF = 987654321

visited = [INF for _ in range(1000001)]

# 큐에 현재 위치 넣고, visited에 0 넣었음
cur = n
queue = deque([cur])
visited[cur] = 0

while (queue):
    # 3가지 방법 다 넣기

    # 지금 꺼낸거
    cur = queue.popleft()

    if (cur== k):
        answer = visited[cur]
        break

    # 안 같으면, -1 +1 *2
    if (cur -1 >= 0):
        if (visited[cur-1] == INF):
            visited[cur-1] = visited[cur] + 1
            queue.append(cur-1)
    if (cur+1 < 1000001):
        if (visited[cur+1] == INF):
            visited[cur+1] = visited[cur] + 1
            queue.append(cur+1)
    if (2*cur < 1000001):
        if (visited[2*cur] == INF):
            visited[2*cur] = visited[cur] + 1
            queue.append(2*cur)


print(answer)