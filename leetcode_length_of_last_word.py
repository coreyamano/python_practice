def lengthOfLastWord(str):
    length = 0
    word_list = str.split()
    length = len(word_list[-1])
    return length

print(lengthOfLastWord('   fly me   to   the moon  '))