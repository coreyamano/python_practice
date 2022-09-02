# 1. Reverse String
# Write a function that returns the reverse of a given string.
# Input: “abcde”
# Output: “edcba”

from cgi import test
from operator import is_
from re import I


def reverse_string(word):
    reversed_word = ""
    i = -1
    while i >= len(word) * -1:
        reversed_word += word[i]
        i -= 1
    return reversed_word


input_word = "abcde"
print(reverse_string(input_word))

# 2. Show Me The Money
# Description
# Given a string, write a function that returns true if the “$” character is contained within the string or false if it is not.
# Input: “i hate $ but i love money i know i know im crazy”
# Output: true
# Input: “abcdefghijklmnopqrstuvwxyz”
# Output: false


def show_me_money(string):
    if "$" in string:
        return True
    else:
        return False


money_string = "i hate $ but i love money i know i know im crazy"
no_money_string = "abcdefghijklmnopqrstuvwxyz"

print(show_me_money(money_string))
print(show_me_money(no_money_string))

# 3. Alternate Capitals

# Description
# Given a string, write a function that returns a copy of the original string that has every other character capitalized. (Capitalization should begin with the second character.)
# Input: “hello, how are your porcupines today?”
# Output: “hElLo, HoW ArE YoUr pOrCuPiNeS ToDaY?”


def alternate_capitals(sentence):
    i = 0
    alt_cap = ""
    while i < len(sentence):
        if i == 0:
            alt_cap += sentence[i].lower()
            i += 1
        elif i % 2 == 0:
            alt_cap += sentence[i].lower()
            i += 1
        elif i % 2 != 0:
            alt_cap += sentence[i].upper()
            i += 1
    return alt_cap


alt_cap_sent = "hello, how are your porcupines today?"
print(alternate_capitals(alt_cap_sent))


# 4. First Duplicate Character
# Description
# Given a string, write a function that returns the first occurence of two duplicate characters in a row, and return the duplicated character.
# Input: “abcdefghhijkkloooop”
# Output: “h”
def find_first_dupe(input_sent):
    output_letter = ""
    let1 = 0
    let2 = 1
    while let2 < len(input_sent):
        if input_sent[let1] == input_sent[let2]:
            output_letter = input_sent[let1]
            return output_letter
        let1 += 1
        let2 += 1


test_dupe_sent = "abcdefghhijkkloooop"
print(find_first_dupe(test_dupe_sent))

# 5. Palindrome
# Description
# Given a string, write a function that returns true if it is a palindrome, and false if it is not. (A palindrome is a word that reads the same both forward and backward.)
# Input: “racecar”
# Output: true
# Input: “baloney”
# Output: false


def is_palindrome(test_word):
    i = -1
    palindrome_test = ""
    while i >= len(test_word) * -1:
        palindrome_test += test_word[i]
        i -= 1
    if palindrome_test == test_word:
        return True
    else:
        return False


test_case1 = "racecar"
test_case2 = "baloney"
print(is_palindrome(test_case1))
print(is_palindrome(test_case2))

# 6. Hamming ->
# Description
# Given two strings of equal length, write a function that returns the number of characters that are different between the two strings.
# Input: "ABCDEFG", "ABCXEOG"
# Output: 2
# Explanation: While the A, B, C, E, and G are in the same place for both strings, they have different characters in the other spaces. Since there are 2 such spaces that are different(the D and F in the first string), we return 2.
# Input: "ABCDEFG", "ABCDEFG",
# Output: 0


def hamming(word1, word2):
    i = 0
    diff_letters = 0
    while i < len(word1):
        if word1[i] != word2[i]:
            diff_letters += 1
        i += 1
    return diff_letters


str1 = 'ABCDEFG'
str2 = 'ABCXEOG'
str3 = 'ABCDEFG'
str4 = 'ABCDEFG'

print(hamming(str1, str2))
print(hamming(str3, str4))

# 7. Reverse Words

# Description
# Given a string of words, write a function that returns a new string that contains the words in reverse order.
# Input: “popcorn is so cool isn’t it yeah i thought so”
# Output: “so thought i yeah it isn’t cool so is popcorn”


def reverse_words(sentence):

    words_in_reverse = []
    words_in_reverse = sentence.split()

    reverse_sentence = ""
    i = -1
    while i >= len(words_in_reverse) * -1:
        reverse_sentence += words_in_reverse[i] + " "
        i -= 1
    return reverse_sentence


test_reverse_sent = "popcorn is so cool isn’t it yeah i thought so"
print(reverse_words(test_reverse_sent))
