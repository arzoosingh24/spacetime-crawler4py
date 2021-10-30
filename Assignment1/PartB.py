from PartA import *
def intersectionOfFiles(file1, file2):
    # O(n). tozenizing is O(n) + computing frequency is O(n)
    # converting to set then list of O(n) + O(n). computing frequency
    # again is O(n)
    file1 = list(set(computeWordFrequencies(tokenize(file1)).keys()))
    file2 = list(set(computeWordFrequencies(tokenize(file2)).keys()))
    f = computeWordFrequencies(file1 + file2)

    count = 0
    for word, freq in f.items(): # O(n)
        if freq > 1: 
            count += 1
    return count

if __name__ == "__main__":
    file1 = ""
    file2 = ""

    for filename in sys.argv[1:]:
        if file1 == "":
            file1 = filename
        else:
            file2 = filename
        
    print(intersectionOfFiles(file1, file2))
