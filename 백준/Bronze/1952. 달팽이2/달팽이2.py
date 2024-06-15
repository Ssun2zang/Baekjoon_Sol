m, n = map(int, input().split())
add = 0 if m<=n else 1
print((min(m,n)-1)*2+add)