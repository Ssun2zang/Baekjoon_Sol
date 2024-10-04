# 초기에 {0}, ... {n} 이 n+1 집합을 이룸
# 합집합 연산과 두 원소가 같은 집합에 포함 여부 확인 연산 수행

#m은 연산의 개수
# 합집합 -> 0 a b
# 두 원소가 같은 집합에 포함되는지 1 a b 
# a랑 b는 n이하의 자연수 또는 0, 같을 수도 있음

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

answers = []

arr = [i for i in range(n+1)]

def find(a):
    if arr[a] == a:
        return a
    else:
        arr[a] = find(arr[a])
        return arr[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a!=b:
        arr[b] = a

def isSameSet(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return("YES")
    else:
        return("NO")

for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    else:
        answers.append(isSameSet(a, b))

for a in answers:
    print(a)