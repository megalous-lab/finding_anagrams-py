# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from ctypes.wintypes import WORD


def find_anagram(word1, word2):
    # [assignment] Add your code here

    return cleanstring(word1)==cleanstring(word2)

def cleanstring(word):
    word = word.lower().split(" ")
    word = sorted("".join(word))

    return word

