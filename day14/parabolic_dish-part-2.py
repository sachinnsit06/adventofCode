import time

def sortString(string,direction):
    sortedList =[]
    for i in string.split("#"):
        if direction == "North" or direction == "West":
            sortSubString = sorted(i)[::-1]
        else:
            sortSubString = sorted(i)
        sortedList.append(''.join(sortSubString))
        sortedList.append("#")
    rtrString = "".join(sortedList)
    return rtrString[:len(string)]


def tiltDish(inputData,direction):
    #tanspose --> columns become row and it becomes easy to move 'O' by transposing columns into 'rows string' for North and South tilt
    if direction == "North" or direction == "South":
        rotatedData = list(map("".join, zip(*inputData)))
        
    else:
        rotatedData = inputData

    SortedList= []
    for i in rotatedData:
        sorted_result = sortString(i,direction)
        SortedList.append(list(sorted_result))

    #Transpose again as the columns are now sorted 
    if direction == "North" or direction == "South":
        transposedData = list(map(list, zip(*SortedList)))
        OutPutAfterMove = [''.join(row) for row in transposedData]
    else:
        OutPutAfterMove = [''.join(row) for row in SortedList]
    
    return OutPutAfterMove

#start Here
st = time.time()
tiltedDishOccurence = {}
inputData = open(r"C:\Users\user\python\adventOfCode\adventOfCode\day14\input.txt", 'r').read().splitlines()
for run in range(1,1000000000):
    for direction in ["North", "West",  "South", "East"]:
        afterMove = tiltDish(inputData,direction)
        inputData = afterMove
    
    occurence = ''.join(inputData)      
    if tiltedDishOccurence.get(occurence, 0) == 1:
        print("This state of dish has been seen before", "spinCyle :", run)
        break
    else:
        tiltedDishOccurence[occurence] = 1
            

distance_north_south = len(inputData[0])
load = 0
for eachRow in inputData:
    no_of_rocks = eachRow.count('O')
    load = load + no_of_rocks*distance_north_south
    distance_north_south = distance_north_south -1 
print("Final Load is", load)

et = time.time()
elapsed = et - st
print('Execution time:', elapsed, 'seconds')
