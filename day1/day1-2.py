data = open("./day1/input.txt").readlines()

sum = 0
stringNums = {"one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}

for line in data:
    first = last = -1 
    firstIndex = lastIndex = -1
    length = len(line)
        # Fist and last numbers 
    for i in range(length-1, -1, -1):
        if(line[i].isnumeric()):
            last = line[i]
            lastIndex = i
            break
    for i in range(length):
        if(line[i].isnumeric()):
            first = line[i]
            firstIndex = i
            break

        # First and last considering the numeric vs Alphabetical
    for string in stringNums.keys():
        index = line.find(string, 0, firstIndex+1)
        while index != -1:
            if(index < firstIndex):
                first = stringNums[string]
                firstIndex = index
            index = line.find(string, index+1, firstIndex+1)
        
        index = line.find(string, lastIndex, length+1)
        while index != -1:
            if(index > lastIndex):
                last = stringNums[string]
                lastIndex = index
            index = line.find(string, index+1, length+1)
    sum += (int(first + last))
    print("Line: ", line, "First: ", first, "Last: ", last, "Combined: ", int(first + last) )
print("The sum is: ", sum)