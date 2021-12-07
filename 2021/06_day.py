#line = input()
line = (input()).split(",")
fishct = [0 for i in range(9)]

while len(line):
    for val in line:
        num = int(val)
        fishct[num] += 1

    line = (input()).split()

for blah in range(256):
    newfc= [ 0 for v in range(9)]
    for i in range(len(fishct)):
        if i == 0:
            newfc[6] += fishct[i]
            newfc[8] += fishct[i]
        else:
            newfc[i-1] += fishct[i]
    fishct = newfc
    if blah == 79:
        print("Day 6a:", sum(fishct))


print("Day 6b:",sum(fishct))
