# 효율적인 관리를 위해 학생마다 고유 학생 번호를 부여
# 학생 번호는 0-9로 이루어진 문자열
# 학생 번호는 서로 다르고 길이가 모두 같음
# 학생 번호가 주어졌을 때, 뒤에서 k자리만 추려서 남겨 놓으려고 함
# 최소의 k를 구하기

# N : 학생의 수
N = int(input())

# set나 사전을 쓰면 쉽게 풀릴 듯함

numbers = []

for _ in range(N):
    numbers.append(input())

for k in range(len(numbers[0])):
    backNums = set()
    for n in numbers:
        backNums.add(n[-k-1:])
    if len(backNums) == len(numbers):
        print(k+1)
        break