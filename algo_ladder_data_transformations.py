# 1. ETL #1


# Description
# You are given two parameters, an array and a number. Return a hash whose keys are each of the values from 
# the array parameter, and whose values are the number parameter.

# Input:

# First argument: ["a", "e", "i", "o", "u"]
# Second argument: 1

# Output:

# {
# 'a' => 1,
# 'e' => 1,
# 'i' => 1,
# 'o' => 1,
# 'u' => 1
# }

def etl_1(arr, num):
    etl_dict = {}
    for n in arr:
        etl_dict[n] = num
    return etl_dict

print(etl_1(["a", "e", "i", "o", "u"],1))

# 2. Flatten Hash

# Description
# Given a hash, return a flat array containing all the hash’s keys and values.

# Input: {“a” => 1, “b” => 2, “c” => 3, “d” => 4}
# Output: [“a”, 1, “b”, 2, “c”, 3, “d”, 4]

def flatten_hash(dict):
    arr = []
    for n in dict:
        arr.append(n)
        arr.append(dict[n])
    return arr

print(flatten_hash({'a':1,'b':2,'c':3,'d':4}))


# 3. Flip Hash

# Description
# Given a hash, create a new hash that has the keys and values switched.

# Input: {"a" => 1, "b" => 2, "c" => 3}
# Output: {1 => "a", 2 => "b", 3 => "c"}

def flip_hash(dict2):
    flipped_dict2 = {}
    for n in dict2:
        flipped_dict2[dict2[n]] = n
    return flipped_dict2

print(flip_hash({"a" : 1, "b" : 2, "c" : 3}))

# 4. ETL #2

# Description
# You are given a hash in format #A, and you are to return the same data as a hash using format #B, 
# as specified below:

# Input:

# {
# 1 => ["A", "E", "I", "O", "U"]
# }

# Output:

# {
# 'a' => 1,
# 'e' => 1,
# 'i' => 1,
# 'o' => 1,
# 'u' => 1
# }
# Input:

# {
# 1 => ["A", "E"],
# 2 => ["D", "G"]
# }

# Output:

# {
# 'a' => 1,
# 'd' => 2,
# 'e' => 1,
# 'g' => 2
# }

# Input:

# {
# 1 => ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
# 2 => ["D", "G"],
# 3 => ["B", "C", "M", "P"],
# 4 => ["F", "H", "V", "W", "Y"],
# 5 => ["K"],
# 8 => ["J", "X"],
# 10 => ["Q", "Z"]
# }

# Output:

# {
# 'a' => 1,
# 'b' => 3,
# 'c' => 3,
# 'd' => 2,
# 'e' => 1,
# 'f' => 4,
# 'g' => 2,
# 'h' => 4,
# 'i' => 1,
# 'j' => 8,
# 'k' => 5,
# 'l' => 1,
# 'm' => 3,
# 'n' => 1,
# 'o' => 1,
# 'p' => 3,
# 'q' => 10,
# 'r' => 1,
# 's' => 1,
# 't' => 1,
# 'u' => 1,
# 'v' => 4,
# 'w' => 4,
# 'x' => 8,
# 'y' => 4,
# 'z' => 10
# }

def etl_ver2(hash_arr):
    map_hash_arr = {}
    for n in hash_arr:
        for m in hash_arr[n]:
            w = m.lower()
            map_hash_arr[w]= n
    return map_hash_arr

print(etl_ver2({
1 : ["A", "E"],
2 : ["D", "G"]
}))

# 5. Complete the Data II
# Description
# Given an array of social media posts and an array of users, return a list of posts (as an array of hashes) 
# that replaces the submitted_by id number as the person's actual name.

# For example, given this array of posts (note that the submitted_by is an id number):

# [
# {title: 'Me Eating Pizza', submitted_by: 231, likes: 1549},
# {title: 'i never knew how cool i was until now', submitted_by: 989, likes: 3},
# {title: 'best selfie evar!!!', submitted_by: 111, likes: 1092},
# {title: 'Mondays are the worst', submitted_by: 403, likes: 644}
# ]

# And this array of users:

# [
# {user_id: 403, name: "Aunty Em"},
# {user_id: 231, name: "Joelle P."},
# {user_id: 989, name: "Lyndon Johnson"},
# {user_id: 111, name: "Patti Q."},
# ]

# Return the array of posts as follows:

# [
# {title: 'Me Eating Pizza', submitted_by: "Joelle P.", likes: 1549},
# {title: 'i never knew how cool i was until now', submitted_by: "Lyndon Johnson", likes: 3},
# {title: 'best selfie evar!!!', submitted_by: "Patti Q.", likes: 1092},
# {title: 'Mondays are the worst', submitted_by: "Aunty Em", likes: 644}
# ]

def complete_data2(arr1,arr2):
    for n in arr1:
        for m in arr2:
            if n['submitted_by'] == m['user_id']:
                n['submitted_by'] = m['name']
    return arr1

print(complete_data2(
[
{'title': 'Me Eating Pizza', 'submitted_by': 231, 'likes': 1549},
{'title': 'i never knew how cool i was until now', 'submitted_by': 989, 'likes': 3},
{'title': 'best selfie evar!!!', 'submitted_by': 111, 'likes': 1092},
{'title': 'Mondays are the worst', 'submitted_by': 403, 'likes': 644}
],
[
{'user_id': 403, 'name': "Aunty Em"},
{'user_id': 231, 'name': "Joelle P."},
{'user_id': 989, 'name': "Lyndon Johnson"},
{'user_id': 111, 'name': "Patti Q."},
]

))

# 6. Book Organizer
# Description
# Given a list of books provided in this format:

# [
# {title: "The Lord of the Rings", author: "J. R. R. Tolkien", year: 1954 },
# {title: "To Kill a Mockingbird", author: "Harper Lee", year: 1960 },
# {title: "1984", author: "George Orwell", year: 1949 },
# {title: "Go Set a Watchman", author: "Harper Lee", year: 2015 },
# {title: "The Hobbit", author: "J. R. R. Tolkien", year: 1937 },
# {title: "The Great Gatsby", author: "F. Scott Fitzgerald", year: 1925 },
# {title: "The Two Towers", author: "J. R. R. Tolkien", year: 1954 }
# ]

# return the data in this new author-centric format:

# { "J. R. R. Tolkien" => [
# {title: "The Lord of the Rings", year: 1954 },
# {title: "The Hobbit", year: 1937 },
# {title: "The Two Towers", year: 1954 }
# ],
# "Harper Lee" => [
# {title: "To Kill a Mockingbird", year: 1960 },
# {title: "Go Set a Watchman", year: 2015 }
# ],
# "George Orwell" => [
# {title: "1984", year: 1949 }
# ],
# "F. Scott Fitzgerald" => [
# {title: "The Great Gatsby", year: 1925 }
# ]
# }

# def book_organizer(books):
#     by_authors = {}
#     book_list = []
#     books_written = {}
#     i = 0
#     for n in books:
#         print(n['author'])
#         while i < len(books):
#             if n['author'] == books[i]['author']:
#                 books_written[n] = books[n]['title','year']
#             i += 1
#             by_authors[n['author']] = books_written
#     return by_authors
    

# print(book_organizer( [
# {'title': "The Lord of the Rings", 'author': "J. R. R. Tolkien", 'year': 1954 },
# {'title': "To Kill a Mockingbird", 'author': "Harper Lee", 'year': 1960 },
# {'title': "1984", 'author': "George Orwell", 'year': 1949 },
# {'title': "Go Set a Watchman", 'author': "Harper Lee", 'year': 2015 },
# {'title': "The Hobbit", 'author': "J. R. R. Tolkien", 'year': 1937 },
# {'title': "The Great Gatsby", 'author': "F. Scott Fitzgerald", 'year': 1925 },
# {'title': "The Two Towers", 'author': "J. R. R. Tolkien", 'year': 1954 }
# ]))

# 7. ETL #3

# Description
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

# Return a new array of videos in the following format, and only include videos that have at least 100 views:

# [
# {title: 'How to Seem Perfect', views: 111, author_name: 'Teena Burgess' }
# {title: 'Review of the New "Unbreakable Mug"', views: 202, author_name: 'Ichabod Loadbearer' },
# ]

def etl3(vids,authors):
    vids_100 = []
    list_vids = {}
    for n in vids:
        for m in authors:
            if n['author_id'] == m['id']:
                n['author_name'] = m['first_name'] + ' ' + m['last_name']
    for n in vids:
        if n['views'] >= 100:
            list_vids = {'title':n['title'],'views':n['views'],'author_name':n['author_name']}
            vids_100.append(list_vids)
    return vids_100

print(etl3(
    [
{'title': 'How to Make Wood', 'author_id': 4, 'views': 6},
{'title': 'How to Seem Perfect', 'author_id': 4, 'views': 111},
{'title': 'Review of the New "Unbreakable Mug"', 'author_id': 2, 'views': 202},
{'title': 'Why Pigs Stink', 'author_id': 1, 'views': 12}
], 
[
{'id': 1, 'first_name': 'Jazz', 'last_name': 'Callahan'},
{'id': 2, 'first_name': 'Ichabod', 'last_name': 'Loadbearer'},
{'id': 3, 'first_name': 'Saron', 'last_name': 'Kim'},
{'id': 4, 'first_name': 'Teena', 'last_name': 'Burgess'},
]
))
