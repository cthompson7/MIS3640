fin = open('words.txt')
line = fin.readline()
word = line.strip()
# print(word)

# counter = 0
# for line in fin:
    # word = line.strip()
    # counter = counter + 1
    # print(word)

def read_long_words():
    """
    prints only the words with more than 20 characters
    """
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

# read_long_words()

def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter “e” in it.
    """
    for letter in word:
    #     # if i == 'e' or "E":
    #     if letter.lower() == "e":
    #         return False
    # return True
        return not "e" in word.lower()

# print(has_no_e('Babson'))
# print(has_no_e('College'))
# print(has_no_e("Epslon"))


def avoids(word, forbidden):
    """
    takes a word and a string of forbidden letters, and that returns True
    if the word doesn’t use any of the forbidden letters.
    """
    for letters in word:
        if letters in forbidden:
            return False
    return True

# print(avoids('Babson', 'ab'))
# print(avoids('College', 'ab'))


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    for letters in available:
        if letters in word:
            return True
        else:
            return False


# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for letters in required:
        if letters in word:
            return True
        else:
            return False


# print(uses_all('Babson', 'abs'))
# print(uses_all('college', 'abs'))


# def is_abecedarian(word):
#     """
#     returns True if the letters in a word appear in alphabetical order
#     (double letters are ok).
#     """
#     previousLetter = word[0]
#     for letter in word:
#         if letter < previousLetter:
#             return False
#         previousLetter = letter
#     return True

# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))


# Exercise 2
# Rewrite is_abecedarian using recursion

# def is_abecedarian(word):
#     """
#     returns True if the letters in a word appear in alphabetical order
#     (double letters are ok).
#     """
#     x = len(word)
#     if x==1:
#         return True
#     elif word[x-2] > word[x-1]:
#         return False
#     else:
#         return is_abecedarian(word[:x-1])

# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))


# Rewrite is_abecedarian using while loop.
def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    n = 0
    while n < len(word)-1:
        if (ord(word[n+1]) - 96) < (ord(word[n]) - 96):
            return False
        n = n + 1
    return True

# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))
