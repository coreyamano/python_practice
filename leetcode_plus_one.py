def plus_one(arr):
    plus = []
    num = ''
    for n in arr:
        num += str(n)
    num = int(num) + 1
    for y in str(num):
        plus.append(y)
    return plus

print(plus_one([1,2,3]))
print(plus_one([9]))