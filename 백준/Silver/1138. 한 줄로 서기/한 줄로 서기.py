n = int(input())
arr = list(map(int, input().split()))
# print(arr)
answer = []
per = n
for i in reversed(arr):
    answer.insert(i, per)
    # print(i, per)
    per-=1
print(*answer)