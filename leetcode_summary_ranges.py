# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in 
# the array exactly. That is, each element of nums is covered by exactly 
# one of the ranges, and there is no integer x such that x is in one of the 
# ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b

def summary_ranges(nums):
    i = 0
    start_val = 0
    t = 0
    end_val = 0
    summary = []


    while i < len(nums):
        if nums[i] == nums[i + 1] - 1:
            start_val = nums[i]

            continue
        else:

