def one_bits(num):
    count = 0
    for n in str(num):
        if n == '1':
            count +=1
    return count

print(one_bits(11111111111111111111111111111101))