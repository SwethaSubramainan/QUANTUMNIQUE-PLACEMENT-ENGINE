def maxSubArray(nums):
    
    current = nums[0]
    maximum = nums[0]
    
    start = 0
    end = 0
    temp_start = 0

    for i in range(1, len(nums)):
        
        if nums[i] > current + nums[i]:
            current = nums[i]
            temp_start = i
        else:
            current = current + nums[i]
        
        if current > maximum:
            maximum = current
            start = temp_start
            end = i

    return maximum, nums[start:end+1]


arr = list(map(int, input("Enter elements: ").split()))

max_sum, subarray = maxSubArray(arr)

print(max_sum)
print(subarray)