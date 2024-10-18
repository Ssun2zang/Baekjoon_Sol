# 상근이는 나무 M 미터가 필요
# 나무 한 줄에 대한 벌목 허가

# 높이 H를 지정
# 연속된 나무를 모두 절단함
# 높이가 H보다 크면 위 ㅅ부분이 잘림

# 나무가 필요한 만큼만 가져가고 싶음
# 적어도 M 미터의 나무를 가져가기 위해 필요한 높이의 최댓값 구하기
# 이진 탐색

import sys
input = sys.stdin.readline


N, M = map(int, input().split())

trees = list(map(int, input().split()))

# 이진 탐색 문제는 함수로 푸는게 좋음
def canGet(t, M):
    for tree in trees:
        if tree - t > 0:
            M -= (tree - t)
        
        if M <= 0:
            return True
    return False

# 최대의 타겟을 구해야 함
answer = 0
start = 1
end = 2_000_000_000

while (start <= end):
    mid = (start + end)//2
    if canGet(mid, M):
        start = mid + 1
        answer = max(answer, mid)
    else:
        end = mid -1

print(answer)