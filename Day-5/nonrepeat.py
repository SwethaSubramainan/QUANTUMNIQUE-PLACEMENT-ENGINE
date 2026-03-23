def first_repeat(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None


arr = list(map, int(input(). split())) 
print(first_repeat(arr))