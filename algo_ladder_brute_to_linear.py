# 1. Array Intersection

# Given two arrays, return a new array that contains the intersection of the two arrays. The intersection 
# means the values that are contained in both of the arrays. Do not use the "&", or any built-in intersection 
# methods.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Input: [1, 2, 3, 4, 5], [1, 3, 5, 7, 9]
# Output: [1, 3, 5]


from operator import truediv


def array_intersect(arr1,arr2):
    inter = []
    for n in arr1:
        for m in arr2:
            if n == m:
                inter.append(n)
    return inter

print(array_intersect([1, 2, 3, 4, 5], [1, 3, 5, 7, 9]))

# 2. Array Subset
# Description
# Given two arrays, determine whether one is a subset of the other. It is considered a subset if all 
# the values in one array are contained within the other.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Input: [1, 2, 3, 4, 5, 6], [6, 3, 2]
# Output: true

# Input: [1, 2, 3, 4, 5, 6], [6, 3, 7]
# Output: false

def arr_subset(arr1,arr2):
    match = []
    if len(arr1) <= len(arr2):
        for n in arr1:
            for m in arr2:
                if n == m:
                    match.append(n)
    elif len(arr2) < len(arr1):
        for n in arr2:
            for m in arr1:
                if n == m:
                    match.append(n)
    if match == arr1 or match == arr2:
        return True
    else:
        return False

print(arr_subset([1, 2, 3, 4, 5, 6], [6, 3, 2]))
print(arr_subset([1, 2, 3, 4, 5, 6], [6, 3, 7]))


# 3. Array Duplicate
# Description
# A given array has one pair of duplicate values. Return the first duplicate value.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Input: [5, 2, 9, 7, 2, 6]
# Output: 2

def find_dupe(arr):
    dupe = 0
    i = 1
    while i < len(arr):
        for n in arr:
            if arr[i] == n:
                return n
        i += 1
    
print(find_dupe([5, 2, 9, 7, 2, 6]))

# 4. Missing Letter
# Description
# A given string contains all the letters from the alphabet except for one. Return the missing letter.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Input: “The quick brown box jumps over a lazy dog”
# Output: “f”

def missing_letter(str):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in str.lower():
        if letter in alpha:
            alpha.remove(letter)
    return alpha

print(missing_letter('The quick brown box jumps over a lazy dog'))


# 5. First Unique Character
# Description
# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, 
# return -1.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Examples:

# s = "leetcode"
# return 0.
# (The "l" is the first character that only appears once in the string, and appears at index 0.)

# s = "loveleetcode",
# return 2.
# (The "l" and "o" are repeated, so the first non-repeating character is the "v", which is at index 2.)

# Note: You may assume the string contain only lowercase letters.

# 6. Two Sum II
# Description
# This is the same exercise as Two Sum I, but you must now solve it in linear time.

# Given an array of numbers, return a new array containing just two numbers (from the original array) 
# that add up to the number 10. If there are no two numbers that add up to 10, return false.

# Input: [2, 5, 3, 1, 0, 7, 11]
# Output: [3, 7]

# Input: [1, 2, 3, 4, 5]
# Output: false (While 1, 2, 3, and 4 altogether add up to 10, we're seeking just one pair of numbers.)

# 7. ETL #4

# Description
# This is very similar to ETL #3, but you must now accomplish the task in linear time (O(N)).

# Given an array of Youtube videos, for example:

# [
# {title: 'How to Make Wood', author_id: 4, views: 6},
# {title: 'How to Seem Perfect', author_id: 4, views: 111},
# {title: 'Review of the New "Unbreakable Mug"', author_id: 2, views: 202},
# {title: 'Why Pigs Stink', author_id: 1, views: 12}
# ]

# and an array of authors, for example:

# [
# {id: 1, first_name: 'Jazz', last_name: 'Callahan'},
# {id: 2, first_name: 'Ichabod', last_name: 'Loadbearer'},
# {id: 3, first_name: 'Saron', last_name: 'Kim'},
# {id: 4, first_name: 'Teena', last_name: 'Burgess'},
# ]

# Return a new array of videos in the following format, and only include videos that have at least 
# 100 views:

# [
# {title: 'How to Seem Perfect', views: 111, author_name: 'Teena Burgess' }
# {title: 'Review of the New "Unbreakable Mug"', views: 202, author_name: 'Ichabod Loadbearer' },
# ]

