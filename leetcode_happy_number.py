def happy_number(num):
    result = num
    sum = 0

    while result != 1 and len(str(result)) != 1:
        for n in str(result):
            sum += int(n)**2
        result = sum
        sum = 0

    if result == 1:
        return True
    else:
        return False

    
print(happy_number(19))
print(happy_number(2))

