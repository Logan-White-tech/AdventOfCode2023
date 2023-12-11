input = open("day1\input.txt")
data = input.read().splitlines()
sum = 0
for line in data:
    first, last = -1
    for i in range(len(line)-1, -1, -1):
        if(line[i].isnumeric()):
            last = line[i]
            break
    for i in range(len(line)):
        if(line[i].isnumeric()):
            first = line[i]
            break
    sum += (int(first + last))
    print("Line: ", line, "First: ", first, "Last: ", last)

print("The sum is {sum}", sum)
        
    