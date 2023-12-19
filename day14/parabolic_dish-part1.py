def sort_string_with_O_and_keep_hash(string):
    sortedList =[]
    for i in string.split("#"):
        sortSubString = sorted(i)[::-1]
        sortedList.append(''.join(sortSubString))
        sortedList.append("#")
    rtrString = "".join(sortedList)
    return rtrString[:len(string)]

inputData = open(r"C:\Users\user\python\adventOfCode\adventOfCode\day14\input.txt", 'r').read().splitlines()

#tanspose --> columns become row and it becomes easy to sort
rotatedData = list(map("".join, zip(*inputData)))

rotatedSortedList= []
for i in rotatedData:
    sorted_result = sort_string_with_O_and_keep_hash(i)
    rotatedSortedList.append(list(sorted_result))

#Transpose again as the columns are now sorted 
transposedData = list(map(list, zip(*rotatedSortedList)))

distance_north_south = len(rotatedSortedList[0])
load = 0
for eachRow in transposedData:
    no_of_rocks = eachRow.count('O')
    load = load + no_of_rocks*distance_north_south
    print("Load at ", distance_north_south, " is ", load)
    distance_north_south = distance_north_south -1 

print("Final Load is", load)
