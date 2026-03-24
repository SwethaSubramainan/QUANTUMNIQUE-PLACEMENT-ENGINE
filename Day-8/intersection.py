arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
res= list(set(arr1).intersection(set(arr2)))
print(res)