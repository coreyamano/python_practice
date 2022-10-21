# Given an array of integers nums and an integer target, return indices of the two numbers such that they 
# add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.

def two_sum(nums,targ):
    output = []
    i = 0
    t = 1
    while i <= len(nums)-1:
        while t < len(nums):
            if i != t:
                if nums[i] + nums[t] == targ:
                    output.append(i)
                    output.append(t)
                    return output
                else:
                    t += 1
            else:
                t += 1        
        t = i + 1
        i +=1    


print(two_sum([11,15,2,7],9))
print(two_sum([3,2,4],6))
print(two_sum([3,3],6))

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]