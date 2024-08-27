# 새로운 언어 AC를 만듦

# AC는 정수 배열에 연산을 하기 위해 만듦

# R - 뒤집기 (수의 순서를 뒤집음)
# D - 버리기 (첫 번째 수를 버림) -> 배열이 비어있는데 D를 사용하면 에러 : error 출력

from collections import deque


def funcfunction(arr, _cmd):
    is_reversed = False
    n = len(arr)
    for c in _cmd:
        if c == 'R':
            is_reversed= not is_reversed
        else: # D일 때
            if (n > 0):
                n-=1
                if is_reversed:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                return "error"
    arr = list(arr)
    if len(arr) == 0:
        return "[]"
    ans = "["
    arr = arr if not is_reversed else list(reversed(arr))
    for idx in range(len(arr)):
        ans += str(arr[idx])
        ans += ","
    ans = ans[:-1]
    ans += "]"
    return ans


T = int(input())
answers = []
for _ in range(T):
    _cmd = input()
    n = int(input())
    if n != 0:
        arr = deque(map(int, input()[1:-1].split(',')))
    else:
        input()
        arr = []

    answers.append(funcfunction(arr, _cmd))

for a in answers:
    print(a)
