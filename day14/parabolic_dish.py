def sort_string_with_O_and_keep_hash(string):
    print(string)
    sortedList =[]
    print(len(string.split("#")))
    for i in string.split("#"):
        sortSubString = sorted(i)[::-1]
        sortedList.append(''.join(sortSubString))
        sortedList.append("#")
    rtrString = "".join(sortedList)
    print(rtrString[:len(string)])
    return rtrString[:len(string)]



inputData = open(r"C:\Users\user\python\adventOfCode\adventOfCode\day14\input.txt", 'r').read().splitlines()


mappedList = list(map("".join, zip(*inputData)))

rotatedList= []
for i in mappedList:
    sorted_result = sort_string_with_O_and_keep_hash(i)
    #print(sorted_result)
    rotatedList.append(list(sorted_result))
    print("\n")

print(list(zip(rotatedList)))