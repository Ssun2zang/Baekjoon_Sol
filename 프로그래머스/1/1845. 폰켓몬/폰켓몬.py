# N마리 중, N/2마리

# 같은 종류의 폰켓몬은 같은 번호를 가짐

# 가장 많은 폰켓몬 종류 번호의 개수를 리턴하도록 하기

def solution(nums):
    counts = {}
    for i in nums:
        if  i in counts.keys():
            counts[i] += 1
        else:
            counts[i] = 1
    return len(counts.keys()) if len(counts.keys()) < len(nums)//2 else len(nums)//2

print(solution([3, 1, 2, 3]))