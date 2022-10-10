def merge_sorted(arr1, arr2):
    sorted_arr = []
    i = 0
    t = 1
    while len(sorted_arr) <= len(arr1) + len(arr2):
        while i < len(arr1) or t < len(arr2):
            if arr1[i] < arr1[t]:
                sorted_arr.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[t]:
                sorted_arr.append(arr2[t])
                t += 1
    return sorted_arr

print(merge_sorted([1,2,4],[1,3,4]))