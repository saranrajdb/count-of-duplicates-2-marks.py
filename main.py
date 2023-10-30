l=list(map(int,input().split()))
l.sort()
s=sorted(list(set(l)))
print(s)
if len(s)>=2:
    a=l.count(s[len(s)-1])
    b=l.count(s[len(s)-2])
print(a,b)
print(a+b-2)


