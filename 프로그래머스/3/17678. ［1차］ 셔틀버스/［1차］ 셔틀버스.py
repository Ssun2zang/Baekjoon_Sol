def solution(n, t, m, timetable):
    timetable.sort()
    minutetable = []
    for _t in timetable:
        temp = list(map(int, _t.split(":")))
        minutetable.append(temp[0]*60+temp[1])
    print(minutetable)
    
    # 9*60 = 540
    ans = 0
    index = 0
    prev = 0
    now = 540
    for i in range(n):
        if (index>=len(minutetable)):
                break
        print("now는", now)
        last = 0
        ppl = 0
        for j in range(m):
            if (index>=len(minutetable)):
                break
            if (now >= minutetable[index]):
                last = minutetable[index]
                ppl+=1
                index +=1
        print("ppl", ppl)
        if (ppl == m):
            print("으이", minutetable[index-1])
            ans = minutetable[index-1]-1
        else:
            ans = now
        now += t
        print(ans)
            
    temp1 = ""
    hour = ans//60
    if (hour//10 ==0):
        temp1="0"
    minute = ans%60
    temp2=""
    if(minute//10==0):
        temp2="0"
    answer = temp1+str(hour)+":"+temp2+str(minute)
    return answer