# 기능 진도가 100퍼일 때 반영

# 뒷 기능은 앞 기능이 배포될 때 함꼐 배포

# 먼저 배포되어야 하는 순서대로 적힌 작업과 속도가 주어짐

# 배포는 하루에 한 번만 하고, 하루의 끝에 이루어진다고 가정함

# 각 배포마다, 몇 개의 기능이 배포되는지 return

def solution(progresses, speeds):
    rest = [(100-progresses[i]-1)//speeds[i]+1 for i in range(len(progresses))]
    print(rest)
    answer = []
    
    s = [rest[0]]
    prev = rest[0]
    for r in rest[1:]:
        if (prev >= r):
            s.append(r)
        else:
            answer.append(len(s))
            s.clear()
            prev = r
            s.append(r)
    
    if len(s)!= 0:
        answer.append(len(s))

    return answer