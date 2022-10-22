def contains_dupe2(nums,val):
    i = 0
    j = 1
    while i < len(nums):
        while j < len(nums)+1:
            if nums[i]==nums[j]:
                if abs(i - j) <= val:
                    return True
                else:
                    return False
            j += 1
        i += 1
        j = i + 1
    return False

print(contains_dupe2([1,2,3,1],3))
print(contains_dupe2([1,0,1,1],1))
print(contains_dupe2([1,2,3,1,2,3],2))