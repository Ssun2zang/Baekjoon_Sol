# 인접해 있는 모든 문자가 같지 않은 행운의 문자열 만들기
# S를 재배치해서 행운의 문자열이 몇 개인지 맞추기
# 원래도 행운이면 개수에 포함

import sys
input = sys.stdin.readline

letters = [0]*27
answer = 0

S = input()
for c in S[:-1]:
    letters[ord(c)-ord('a')] +=1

def dfs(depth, cur):
    global answer
    if depth == len(S)-1:
        answer += 1
        return 

    for i, v in enumerate(letters):
        if v == 0:
            continue
        if cur != "":
            if cur[-1] == chr(ord('a')+i):
                continue
        letters[i] -=1
        dfs(depth+1, cur + chr(ord('a')+i))
        letters[i] +=1

dfs(0, "")
print(answer)