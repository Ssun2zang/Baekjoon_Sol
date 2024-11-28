import sys
input = sys.stdin.readline

_, m = map(int, input().split())
nums = list(map(int, input().split()))

answers = []
for n in nums:
	if n < m:
            answers.append(n)

for a in answers[:-1]:
    print(a, end=" ")
print(answers[-1])