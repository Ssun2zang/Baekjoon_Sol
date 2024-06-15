k = int(input())
cnt = 0

for i in range(0, k):
    answkd = input()
    answkd_len = len(answkd)
    arr = []
    arr_break = True
    for j in range(1, answkd_len):
        for k in range(0, len(arr)):
            if (answkd[j] == arr[k]):
                arr_break = False
                break

        if(arr_break == False):
            break    

        if (answkd[j-1] == answkd[j]):
            pass
        else:
            arr.append(answkd[j-1])
    if(arr_break == True):
        cnt += 1

print(cnt)