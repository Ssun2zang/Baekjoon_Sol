import sys
input = sys.stdin.readline

answers = set()

for _ in range(10):
    answers.add(int(input())%42)

print(len(answers))