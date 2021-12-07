line = (input()).split()
aim = 0
depth1 = 0
depth2 = 0
forward = 0

while len(line):
    num = int(line[1])
    #print(num)
    if line[0]=="down":
        depth1 += num
        aim += num
    elif line[0]=="up":
        depth1 -= num
        aim -= num
    elif line[0]=="forward":
        forward += num
        depth2 += aim*num

    line = (input()).split()
    
print("Day 2a:",depth1*forward)
print("Day 2b:",depth2 * forward)
