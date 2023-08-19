#Unscramble the words

import os

output = ""
word_list=[]

with open("resources/wordlist.txt") as fp:
    word_list = fp.read().splitlines()

with open("resources/input.txt") as fp:
    allLines = fp.read().splitlines()

    for currentInputRow in allLines:

        for currentWord in word_list:
            if len(currentInputRow) == len(currentWord):
                arrayForInputRow = list(currentInputRow)
                arrayForWord = list(currentWord)
                totalCharFound = 0

                for indexInputRow, inputRowChar  in enumerate(arrayForInputRow):
                    if inputRowChar in arrayForWord:
                        for indexChar, wordChar  in enumerate(arrayForWord):
                            if wordChar == inputRowChar:
                                arrayForWord[indexChar] = ""
                                break
                        #print (arrayForWord, "-", inputRowChar, "-", totalCharFound)
                        totalCharFound = totalCharFound + 1
                    else:
                        break

                if totalCharFound == len(currentInputRow):
                    output += currentWord + ","
print(output[:-1])