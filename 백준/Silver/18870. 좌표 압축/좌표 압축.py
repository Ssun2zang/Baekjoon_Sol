# 좌표를 압축할 거임
# Xi> Xj를 만족하는 > 서로 다른 < Xj의 개수와 같아야한다.
import sys
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

num_set = sorted(list(set(nums)))

num_hash = {key:index for index, key in enumerate(num_set)}
answers = []

for n in nums:
    answers.append(num_hash[n])
    
for a in answers:
    print(a, end=" ")