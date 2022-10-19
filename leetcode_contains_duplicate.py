def contains_duplicate(nums):
    i = 1
    times = 0
    for n in nums:
        while i < len(nums):
            if n == nums[i]:
                return True
            i += 1
        times += 1
        i = 1 + times
    return False

print(contains_duplicate([1,2,3,1]))
print(contains_duplicate([1,2,3,4]))
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))
