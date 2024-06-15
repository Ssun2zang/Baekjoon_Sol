n = int(input())
cnt = 0
for i in range(n):
    str = input()
    arr = []
    temp = ''
    flag = 1
    for j in range(len(str)):
        if temp != str[j]:
            temp = str[j]
            if str[j] in arr:
                flag = 0
                break
            else:
                arr.append(str[j])
    cnt+=flag
print(cnt)