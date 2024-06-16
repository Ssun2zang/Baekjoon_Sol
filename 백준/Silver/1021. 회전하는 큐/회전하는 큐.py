n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
temp = 1
for i in range(len(arr)):
    find = arr[i]
    for j in range(i):
        if arr[j]<arr[i]:
            find -= 1
    move = abs(find-temp) if abs(find-temp)<n-abs(find-temp) else n-abs(find-temp)
    temp = find
    cnt += move
    n-=1

print(cnt)