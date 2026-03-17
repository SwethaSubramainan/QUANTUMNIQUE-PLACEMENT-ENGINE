arr=list(map(int,input().split()))
f=float('-inf')
s=float('-inf')
for num in arr:
    if num>f:
        s=f
        f=num
    elif num>s and num!=f:
        s=num
print(s)