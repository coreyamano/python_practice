def remove_dupes(nums):
    length = 0
    dupes_out = []
    for num in nums:
        if num not in dupes_out:
            dupes_out.append(num)
    length = len(dupes_out)
    return length

print(remove_dupes([1,1,2]))
print(remove_dupes([0,0,1,1,1,2,2,3,3,4]))
