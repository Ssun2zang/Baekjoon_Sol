N, X = map(int, input().split())

visits = list(map(int, input().split()))

sum_val = 0
for i in range(0, X):
    sum_val += visits[i]

max_val = sum_val
cnt = 1

for j in range(X, len(visits)):
    sum_val -= visits[j-X]
    sum_val += visits[j]

    if (sum_val > max_val):
        max_val = sum_val
        cnt = 1
    elif (sum_val == max_val):
        cnt += 1


if(max_val == 0):
    print("SAD")
    exit()
print(max_val)
print(cnt)