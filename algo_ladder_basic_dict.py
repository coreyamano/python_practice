# 1. Most Frequent Letter
# Description
# Given a string, find the most commonly occurring letter.

# Input: “peter piper picked a peck of pickled peppers”
# Output: “p”

def frequent_letter(string):
    letter_dict = {}
    for n in string:
        letter_dict[n] = letter_dict.get(n,0) + 1
    return max(letter_dict, key=letter_dict.get)

print(frequent_letter('peter piper picked a peck of pickled peppers'))

# 2. Count Votes
# Description
# Given an array of strings, return a hash that provides of a count of how many times each string occurs.

# Input: ["Dewey", "Truman", "Dewey", "Dewey", "Truman", "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]

# Output: {"Dewey" => 6, "Truman" => 5}

# Explanation: "Dewey" occurs 6 times in the array, while "Truman" occurs 5 times.

def count_votes(array):
    counted_votes = {}
    for n in array:
        counted_votes[n] = counted_votes.get(n,0) + 1
    return counted_votes

print(count_votes(["Dewey", "Truman", "Dewey", "Dewey", "Truman", "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]))

# 3. Order the Whole Menu

# Description
# Given a hash, where the keys are strings representing food items, and the values are numbers 
# representing the price of each food, return the amount someone would pay if they'd order one of each 
# food from the entire menu.

# Input: {"hot dog" => 2, "hamburger" => 3, "steak sandwich" => 5, "fries" => 1, "cole slaw" => 1, 
# "soda" => 2}

# Output: 14

def count_menu(menu):
    total_cost = 0
    for n in menu:
        total_cost += menu[n]
    return total_cost

print(count_menu({"hot dog":2, "hamburger":3, "steak sandwich":5, "fries":1, "cole slaw":1, 
"soda":2}))

# Explanation: If someone would order one of everything on the menu, they'd pay a total of 14 
# (the sum of all the hash's values).

# 4. Popular Posts

# Description
# Given an array of hashes that represent a list of social media posts, return a new array that only contains 
# the posts that have at least 1000 likes.

# Input: [
# {title: 'Me Eating Pizza', submitted_by: "Joelle P.", likes: 1549},
# {title: 'i never knew how cool i was until now', submitted_by: "Lyndon Johnson", likes: 3},
# {title: 'best selfie evar!!!', submitted_by: "Patti Q.", likes: 1092},
# {title: 'Mondays are the worst', submitted_by: "Aunty Em", likes: 644}
# ]

# Output: [
# {title: 'Me Eating Pizza', submitted_by: "Joelle P.", likes: 1549},
# {title: 'best selfie evar!!!', submitted_by: "Patti Q.", likes: 1092},
# ]


def top_liked(posts):
    only_the_top = []
    for n in posts:
        if n['likes'] >= 1000:
            only_the_top.append(n)
    return only_the_top

print(top_liked([
    {'title': 'Me Eating Pizza', 'submitted_by': "Joelle P.", 'likes': 1549},
    {'title': 'i never knew how cool i was until now', 'submitted_by': "Lyndon Johnson", 'likes': 3},
    {'title': 'best selfie evar!!!', 'submitted_by': "Patti Q.", 'likes': 1092},
    {'title': 'Mondays are the worst', 'submitted_by': "Aunty Em", 'likes': 644}
]))

# 5. RNA Transcription

# Description
# Given a DNA strand, return its RNA complement (per RNA transcription).

# Both DNA and RNA strands are a sequence of nucleotides. Here we're representing the sequences with 
# single-letter characters (e.g. a sample strand may look like: "AGCA".)

# Given a string representing a DNA strand, provide its transcribed RNA strand, according to the following 
# pattern:

# G becomes C
# C becomes G
# T becomes A
# A becomes U

# So based on all this, here's a sample input/output:

# Input: 'ACGTGGTCTTAA'
# Output: 'UGCACCAGAAUU'

def give_rna(dna_string):
    rna_string = ""
    for n in dna_string:
        if n == 'G':
            rna_string += 'C'
        elif n == 'C':
            rna_string += 'G'
        elif n == 'T':
            rna_string += 'A'
        elif n == 'A':
            rna_string += 'U'
    return rna_string

print(give_rna('ACGTGGTCTTAA'))

# 6. Complete the Data I
# Description
# Given an array of social media posts and a hash of users, return a list of posts (as an array of hashes) 
# that replaces the submitted_by id number as the person's actual name.

# For example, given this array of posts (note that the submitted_by is an id number):

# [
# {title: 'Me Eating Pizza', submitted_by: 231, likes: 1549},
# {title: 'i never knew how cool i was until now', submitted_by: 989, likes: 3},
# {title: 'best selfie evar!!!', submitted_by: 111, likes: 1092},
# {title: 'Mondays are the worst', submitted_by: 403, likes: 644}
# ]

# And this hash of users (the key is the id number and the value is the user's real name):

# users = {403 => "Aunty Em", 231 => "Joelle P.", 989 => "Lyndon Johnson", 111 => "Patti Q."}

# Return the array of posts as follows:

# [
# {title: 'Me Eating Pizza', submitted_by: "Joelle P.", likes: 1549},
# {title: 'i never knew how cool i was until now', submitted_by: "Lyndon Johnson", likes: 3},
# {title: 'best selfie evar!!!', submitted_by: "Patti Q.", likes: 1092},
# {title: 'Mondays are the worst', submitted_by: "Aunty Em", likes: 644}
# ]

# 7. Anagrams

# Description
# Given two strings, return true if they are anagrams of each other, and false if they are not. An anagram 
# is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

# Do not use any built-in sort methods.

# Input: “silent”, “listen”
# Output: true

# Input: “frog”, “bear”
# Output: false