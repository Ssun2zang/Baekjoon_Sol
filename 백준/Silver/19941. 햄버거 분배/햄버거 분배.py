# 시간 제한이 매우 짧음
# 사람들은 자기 위치에서 거리가 K 이하여야 먹을 수 있음
# 먹을 수 있는 사람의 최대 수를 구하기

N, K = map(int, input().split())
happy = input()

# 그리디
# 이 문제는 어떻게 풀까? 2N으로 순회하면 될 것 같은데 
# => 햄버거용 순회, 사람용 순회
# 동시에 순회하는 걸 어떻게 구현하지. . .?

hp = -1  # 햄버거 포인터
pp = -1  # 사람 포인터

answer = 0
while hp < N and pp < N:
    while hp < N and happy[hp] != 'H':
        hp += 1
    
    while pp < N and happy[pp] != 'P':
        pp += 1

    # print(hp, pp)
    if (abs(hp-pp)<=K and hp != -1 and pp != -1 and hp < N and pp < N):
        # print("성공")
        answer +=1
        hp +=1
        pp +=1
    else:
        if(hp>pp):
            pp+=1
        else:
            hp+=1

print(answer)