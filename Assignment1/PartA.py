import sys
def tokenize(textFilePath):
    # This runs in linear time O(n) where n is the
    # amount of characters in a file
    tokenList = []
    with open(textFilePath) as fp:
        char = fp.read(1)
        token = ""
        while char:
            ordValue = ord(char)
            if (ordValue >= 48 and ordValue <= 57) or (ordValue >= 97 and ordValue <= 122) or (ordValue >= 65 and ordValue <= 90):
                token += char
            else:
                if token != "":
                    tokenList.append(token)
                    token = ""
            char = fp.read(1)
    return tokenList
def computeWordFrequencies(listOfTokens):
    # Linear time O(n) where n is the length of the list
    counts = dict()
    for word in listOfTokens:
        word = word.lower()
        if word not in counts.keys():
            counts[word] = 1
        else:
            counts[word] += 1
    return counts
def printWordFrequency(dictOfFrequencies):
    # O(nlogn): sorting is nlogn
    for k, v in sorted(dictOfFrequencies.items(), key=lambda item: item[1], reverse = True):
        print(k,"=",v)

if __name__ == "__main__":
    fileInput = ""
    for filename in sys.argv[1:]:
          fileInput = filename
    tokenList = tokenize(fileInput)
    counts = computeWordFrequencies(tokenList)
    printWordFrequency(counts)