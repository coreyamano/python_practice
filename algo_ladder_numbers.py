
# 1. FizzBuzz
# Description
# Write a function that prints out every number from 1 to N, with the following exceptions:
# If the number is divisible by 3, print out "FIZZ".
# If the number is divisible by 5, print out "BUZZ".
# If the number is divisible by both 3 and 5, print out "FIZZBUZZ".

from gettext import find


def fizzbuzz(x):
    x_list = range(1, x+1)
    for n in x_list:
        if n % 3 == 0 and n % 5 == 0:
            print("FIZZBUZZ")
        elif n % 3 == 0:
            print("FIZZ")
        elif n % 5 == 0:
            print("BUZZ")
        else:
            print(n)


# fizzbuzz(3)
# fizzbuzz(15)
# fizzbuzz(5)
# fizzbuzz(4)

# 2. Primes
# Description
# Write a function that returns whether a given number is a prime number.

# === WORK IN PROGRESS ===
# def prime_number(num):
#     check_prime = range(1, num+1)
#     is_prime = False
#     for n in check_prime:
#         if num % n != 0:
#             is_prime = False
#             break
#         else:
#             is_prime = True
#     return is_prime


# print(prime_number(4))
# print(prime_number(5))
# print(prime_number(8))
# print(prime_number(15))
# print(prime_number(144))

# 3. Fibonacci numbers
# Description
# Write a function that gives the Nth number of the Fibonacci Sequence. The Fibonacci sequence begins with 0 and 1, and every number thereafter is the sum of the previous two numbers. So the sequence goes like this:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, and so on until infinity...
# Input: 9
# Output: 21 (as this is the 9th number of the Fibonacci Sequence)

def find_fib_num(num):
    step1 = 0
    step2 = 1
    final_result = 0
    times = 2
    if num == 0:
        final_result = 0
    elif num == 1 or num == 2:
        final_result = 1
    else:
        while times < num:
            final_result = step1 + step2
            step1 = step2
            step2 = final_result
            times += 1
    return final_result


print(find_fib_num(9))


# 4. Leap Year

# Description
# Given a year, report if it is a leap year.
# The tricky thing here is that a leap year in the Gregorian calendar occurs:
# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400
# For example, 1997 is not a leap year, but 1996 is . 1900 is not a leap year, but 2000 is .
# If your language provides a method in the standard library that does this look-up, pretend it doesn't exist and implement it yourself.

# 5. Multiples of 3 and 5
# Description
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def find_sum_of_mult(num):
    final_sum = 0
    range_num = list(range(1,num))
    for n in range_num:
        if n % 3 == 0 or n % 5 == 0:
            final_sum += n
    return final_sum

print(find_sum_of_mult(1000))


# 6. Collatz Conjecture
# Description
# The Collatz Conjecture or 3x+1 problem can be summarized as follows:
# Take any positive integer n. If n is even, divide n by 2 to get n / 2. If n is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the process indefinitely. The conjecture states that no matter which number you start with, you will always reach 1 eventually.
# Given a number n, return the number of steps required to reach 1.
# Examples
# Starting with n = 12, the steps would be as follows:
# 12
# 6
# 3
# 10
# 5
# 16
# 8
# 4
# 2
# 1
# Resulting in 9 steps. So for input n = 12, the return value would be 9.

# 7. Largest Palindrome Product
# Description
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
