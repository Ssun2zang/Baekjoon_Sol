# n개의 퍼즐을 제한 시간 내에 풀어야 함
# 각 퍼즐 -> 난이도, 소요시간이 있음
# 숙련도에 따라 퍼즐을 틀리는 횟수가 바뀜
# 현재 기준 난이도 diff, 소요 시간 time_cur, 이전 소요시간 time_prev
# 숙련도는 level

# 난이도 <= 숙련도 -> 틀리지 않고 time_cur로 해결
# 난이도 > 숙련도, diff - level 번 틀림 -> 틀릴 때마다 time_cur 사용
# -> 추가로, time_prev만큼 시간 써서 이전 문제도 풀고 와야 함 => 틀리지 않음

# 전체 제한 시간 limit가 있음
# 모두 해결하기 위한 숙련도 (level의 최솟값 구하기)

# 이분탐색?
def solution(diffs, times, limit):
    answer = 0
    start = 1
    end = max(diffs)
    
    mid = (start+end)//2
    
    def can_solve(level):
        time = limit
        prev = 0
        for i, d in enumerate(diffs):
            if level >= d:
                time -= times[i]
                prev = times[i]
            else:
                time -= ((times[i]+prev)*(d-level)+times[i])
                prev = times[i]
            if time < 0:
                return False
        if time >= 0:
            return True
        else:
            return False
    
    while(start <= end):
        print(mid)
        if (can_solve(mid)):
            answer = mid
            end = mid - 1
            mid = (start+end)//2
        
        else:
            start = mid + 1
            mid = (start+end)//2
            
    
    return answer