# 8 * 8 체스판
# 열이 A-H, 행은 1-8
# R, K, B, T, RT, LT, RB, LB

# 돌과 같은 곳으로 이동하는 경우 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동함
# 입력으로 킹이 어떻게 움직일지 주어짐 -> 킹이나 돌이 체스판 밖으로 나가는 경우 건너뜀

# 아 행이랑 열 반대로함;;;;;

rowDict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
reverseDict = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H'}
movDict = {'R':(0, 1), 'L':(0, -1), 'B':(-1, 0), 'T': (1, 0), 'RT': (1, 1), 'LT': (1, -1), 'RB':(-1, 1), 'LB':(-1, -1)}

def checkIsValid(a):
    if (a[0]>8 or a[0]<1):
        return False
    elif (a[1]>8 or a[1]<1):
        return False
    return True

# 유효성 검사 함수
def checkIsValidNMov(k, s, mov):
    newKing = (k[0]+mov[0], k[1] +mov[1])
    if (checkIsValid(newKing)):
        # 돌이 유효한지 확인
        if (newKing[0] == s[0] and newKing[1] == s[1]):
            newStone = (s[0]+ mov[0], s[1]+mov[1])
            if (checkIsValid(newStone)):
                return newKing, newStone
            else:
                return k, s
        else:
            return newKing, s
    else:
        return k, s

king, stone, N = input().split()
N = int(N)

# 1 A
king = (int(king[1]), rowDict[king[0]])
stone = (int(stone[1]), rowDict[stone[0]])


for _ in range(N):
    mov = input()
    king, stone = checkIsValidNMov(king, stone, movDict[mov])

# 영어로 바꿔야 함
print(reverseDict[king[1]]+str(king[0]))
print(reverseDict[stone[1]]+str(stone[0]))