# team = 'New England Patriots'
# letter = team[1] #The expression in brackets is called an index.
# print(letter)

# print(team[0])
#
# print(len(team))
#
# print(team[20-1])
#
# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == "O" or letter == "Q":
#         print(letter + 'u' + suffix)
#     print(letter + suffix)
#
# print(team[:11])
# print(team[12:])
#
# team[4:11]
#
# team[0:20:2]
#
# team[::2]
#
# team[::-2]
#
# for i in range(len(team)):
#     if team[i] == "a":
#         print(i)
#
# for i, letter in enumerate(team):
#     print(i, letter)

# def count(s, letter):
#     totalCount = 0
#     for each in s:
#         if each == letter:
#             totalCount = totalCount + 1
#     return totalCount
#
# print(count(team, "a"))




# Exercise 3:
# Read the documentation of the string methods at https://docs.python.org/3/library/stdtypes.html#string-methods.
# You might want to experiment with some of them to make sure you understand how they work. split, strip and replace
# are particularly useful.
#
# The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), the brackets
# indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is
# optional.
#
# Read the examples of String format. https://docs.python.org/3/library/string.html#format-examples

# phrase = "Hello,My name is Christian."
# wordSplit = phrase.split(",")
# for word in wordSplit:
#     print(word)
#
# AnotherPhrase = "             This sentence has spaces."
# wordStrip = AnotherPhrase.strip()
# print(wordStrip)
#
# finalPhrase = "Replace cat with another word."
# wordReplace = finalPhrase.replace("cat", "dog")
# print(wordReplace)


# Exercise 4: cheap is $33, free is $34 !
# 1. You walk into a store where each item is priced according to the letters in its name: 'a' costs $1, 'b' is $2, and
# so on. Write a program that prints a receipt for this wacky store:
#
# bananas $52
# rice $35
# paprika $72
# potato chips $78
# ------------------------
# Total $237

storeItems = ["bananas", "rice", "paprika", "potato chips"]

def printReciept(storeItems):
    totalReciept = 0
    for items in storeItems:
        price = 0
        for i in items:
            price = price + ord(i) - 96
        print("{} ${}".format(items, price))
        totalReciept = totalReciept + price
    print("--------------------")
    print("Total ${}".format(totalReciept))

# printReciept(storeItems)


# 2. Modify your solution to Part 1 to align the prices and add cents. You may assume that "potato chips" is the
# longest item name.

# bananas               $52.00
# rice                  $35.00
# paprika               $72.00
# potato chips          $78.00
# ----------------------------
# Total                $237.00

def printReciept(storeItems):
    totalReciept = 0
    highestLength = len(storeItems[3]) + 16
    for items in storeItems:
        price = 0
        for i in items:
            price = price + ord(i) - 96
        totalPriceString = "${:.2f}".format(price)
        numberOfSpaces = highestLength - len(items) - len(totalPriceString)
        itemLineString = items + " "*numberOfSpaces + totalPriceString
        print(itemLineString)
        totalReciept = totalReciept + price

    overalTotalPriceString = "${:.2f}".format(totalReciept)
    totalAndOTPS = len(overalTotalPriceString) + len("Total")
    longestLine = highestLength - totalAndOTPS
    print("-"*highestLength)
    finalLine = 'Total' + " "*longestLine + overalTotalPriceString
    print(finalLine)

# printReciept(storeItems)


# 3. Modify your Part 2 solution to adapt to the length of the longest name. For example, if you removed potato chips
# from the list of items, it might print:
# bananas          $52.00
# rice             $35.00
# paprika          $72.00
# ------------------------
# Total           $237.00

def printReciept(storeItems):
    totalReciept = 0
    highestLength = len(max(storeItems)) + 16
    for items in storeItems:
        price = 0
        for i in items:
            price = price + ord(i) - 96
        totalPriceString = "${:.2f}".format(price)
        numberOfSpaces = highestLength - len(items) - len(totalPriceString)
        itemLineString = items + " "*numberOfSpaces + totalPriceString
        print(itemLineString)
        totalReciept = totalReciept + price

    overalTotalPriceString = "${:.2f}".format(totalReciept)
    totalAndOTPS = len(overalTotalPriceString) + len("Total")
    longestLine = highestLength - totalAndOTPS
    print("-"*highestLength)
    finalLine = 'Total' + " "*longestLine + overalTotalPriceString
    print(finalLine)

# printReciept(storeItems)
