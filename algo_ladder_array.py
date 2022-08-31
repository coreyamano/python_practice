

# REDUCE SUM
# Write a function that returns the sum of all numbers in a given array.
# NOTE: Do not use any built-in language functions that do this automatically for you.
# Input: [1, 2, 3, 4]
# Output: 10
# Explanation: (1 + 2 + 3 + 4) = 10

def reduce_sum(nums):
    total_sum = 0
    for num in nums:
        total_sum += num
    return total_sum


nums_input = [4, 5, 6, 7]
print(reduce_sum(nums_input))


# SELECT LESS THAN 100
# Description
# Given an array of numbers, write a function that returns a new array that contains all numbers from the original array that are less than 100.
# Input: [99, 101, 88, 4, 2000, 50]
# Output: [99, 88, 4, 50]

def less_than_100(numbers):
    less_than_100_numbers = []
    for num in numbers:
        if num < 100:
            less_than_100_numbers.append(num)
    return less_than_100_numbers


new_list = [99, 101, 88, 4, 2000, 50]
print(less_than_100(new_list))


# MAP: DOUBLE
# Given an array of numbers, write a function that returns a new array whose values are the original array’s value doubled.
# Input: [4, 2, 5, 99, -4]
# Output: [8, 4, 10, 198, -8]

def double_nums(singles):
    doubles = []
    for num in singles:
        doubles.append(num*2)
    return doubles


single_nums = [4, 2, 5, 99, -4]
print(double_nums(single_nums))

# ARRAY MAX
# Write a function that returns the greatest value from an array of numbers.
# Input: [5, 17, -4, 20, 12]
# Output: 20


def find_max(nums2):
    max_num = float('-inf')
    for num in nums2:
        if num > max_num:
            max_num = num
    return max_num


numbers2 = [5, 17, -4, 20, 12]
print(find_max(numbers2))


# REDUCE PRODUCT

# Write a function that accepts an array of numbers and returns the product of all the numbers.
# Input: [1, 2, 3, 4]
# Output: 24
# Explanation: (1 x 2 x 3 x 4) = 24

def reduce_product(nums2):
    final = nums2[0]
    for num in nums2:
        final = final * num
    return final


multiply_nums = [1, 2, 3, 4]

print(reduce_product(multiply_nums))

# REVERSE ARRAY
# Given an array, write a function that returns an array that contains the original array’s values in reverse.
# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]


def reverse_array(reverse_nums):
    i = -1
    output_nums = []
    while i >= len(reverse_nums) * -1:
        output_nums.append(reverse_nums[i])
        i -= 1
    return output_nums


input_nums = [1, 2, 3, 4, 5]
print(reverse_array(input_nums))

# SKIP IT
# Given an array of numbers, write a function that returns a new array in which only select numbers from the original array are included, based on the following details:
# The new array should always start with the first number from the original array. The next number that should be included depends on what the first number is. The first number dictates how many spaces to the right the computer should move to pick the next number. For example, if the first number is 2, then the next number that the computer should select would be two spaces to the right. This number gets added to the new array. If this next number happens to be a 4, then the next number after that is the one four spaces to the right. And so on and so forth until the end of the array is reached.
# Input:
# [2, 1, 3, 2, 5, 1, 2, 6, 2, 7, 1, 5, 6, 3, 2, 6, 2, 1, 2]
# Output:
# [2, 3, 1, 2, 2, 1, 5, 2, 2]


def skip_nums(array):
    i = 0
    output_array = []
    while i < len(array):
        output_array.append(array[i])
        i += array[i]
    return output_array


test_array = [2, 1, 3, 2, 5, 1, 2, 6, 2, 7, 1, 5, 6, 3, 2, 6, 2, 1, 2]

print(skip_nums(test_array))
