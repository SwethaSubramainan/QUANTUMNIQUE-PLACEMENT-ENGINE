def first_non_repeating(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    for num in arr:
        if freq[num] == 1:
            return num

    return -1  
arr = [4,5,1,2,0,4,1,2]

print(first_non_repeating(arr))