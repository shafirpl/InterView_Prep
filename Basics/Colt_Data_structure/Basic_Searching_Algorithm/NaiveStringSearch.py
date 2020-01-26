def naiveStringSearch(bigString,smallString):
    # for java use string.toCharArray()
    if(len(bigString) == 0 or len(smallString) == 0): return 0
    longerString = list(bigString)
    shorterString = list(smallString)
    length = len(shorterString)
    frequency = 0
    totalMatch = 0
    longerWord = 0
    shorterWord = 0

    while(longerWord < len(longerString)):
        if(longerString[longerWord] == shorterString[shorterWord]):
            while(shorterString[shorterWord] == longerString[longerWord]):
                totalMatch += 1
                longerWord += 1
                shorterWord += 1
                if(longerWord>= len(longerString) or shorterWord >= length): break
        if(totalMatch == length): frequency += 1
        shorterWord = 0
        totalMatch = 0
        longerWord += 1

    return frequency

# print(naiveStringSearch('omlomgomlomgomlomg','omg'))




