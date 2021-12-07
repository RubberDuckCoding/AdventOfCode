#line = input()


def markLineDay1(grid, one, two, three, four):
    if one==three: #same x
        for i in range(min(two,four),max(two,four)+1):
            grid[one][i] += 1
    elif two==four: #same y
        for i in range(min(one, three),max(one,three)+1):
            grid[i][two] += 1
    #ignore diagonals


def markLineDay2(grid, one, two, three, four):
    if one==three: #same x
        for i in range(min(two,four),max(two,four)+1):
            grid[one][i] += 1
    elif two==four: #same y
        for i in range(min(one, three),max(one,three)+1):
            grid[i][two] += 1
    else: #include diagonals
        d1 = three-one
        d2 = four-two
        dist = abs(three-one)
        for i in range(dist+1):
            x = one+d1*i/dist
            y = two+(d2*i)/dist
            grid[int(x)][int(y)] += 1


line = (input()).split()
grid1 = [[0 for i in range(1000)] for j in range(1000)]
grid2 = [[0 for i in range(1000)] for j in range(1000)]

while len(line):
    p1x, p1y = line[0].split(",")
    p1x =  int(p1x)
    p1y = int(p1y)
    p2x, p2y = line[2].split(",")
    p2x = int(p2x)
    p2y = int(p2y)
    #m = max(m, p2x, p1x, p2y, p1y)

    markLineDay1(grid1, p1x, p1y, p2x, p2y)
    markLineDay2(grid2, p1x, p1y, p2x, p2y)

    line = (input()).split()

c=0
for row in grid1:
    for i in row:
        if i > 1:
            c+= 1
print("Day 5a:",c)

c=0
for row in grid2:
    for i in row:
        if i > 1:
            c+= 1
print("Day 5b:",c)
