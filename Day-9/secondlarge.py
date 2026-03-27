nums = list(map(int,input().split()))

largest = sec_lar = float('-inf')

for n in nums:
    if n > largest:
        sec_lar = largest
        largest = n
    elif n > sec_lar and n != largest:
        sec_lar = n

print(sec_lar)
