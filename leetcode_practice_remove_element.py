def remove_element(nums,val):
    length = 0
    output = []
    for num in nums:
        if num != val:
            output.append(num)
    length = len(output)
    return length

print(remove_element([3,2,2,3],3))
print(remove_element([0,1,2,2,3,0,4,2],2))