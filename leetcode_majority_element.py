def majority(arr):
    max = 0
    count = {}
    for n in arr:
        count[n] = count.get(n,0) + 1
    return max(count, key=count.get)

print(majority([2,2,1,1,1,2,2]))