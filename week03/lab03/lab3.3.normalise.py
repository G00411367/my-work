# This program reads in a string and strips any leading or trailing spaces
# It also converts all letters to lower case
# It also outputs the length of the original string and the normalised one

rawString = input("please enter a string : ")
normalisedString = rawString.strip().lower()

LrawString = len(rawString)
LnormalisedString = len(normalisedString)

print("That String normalised is : {} ". format(normalisedString))
print("We reduced the input string from {} to {} characters". format(LrawString, LnormalisedString))
