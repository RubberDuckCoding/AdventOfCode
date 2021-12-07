line = (input()).split(",")
numlist = [int(i) for i in line]
line = (input()).split()

boards = []

def addBoard(boards):
    boards.append( [[0 for i in range(5)] for i in range(5)] )

i = 1
while len(line) != 1: #for "end" or "q"

    if not len(line): #ends on 2nd blank line
        if i == 0:
            boards = boards[:-1]
            break
        addBoard(boards)
        i = 0
    else :
        for j in range(5):
            boards[len(boards)-1][i][j] = int(line[j])
        i += 1
    line = (input()).split()

def getRes(board, num):
    s = 0
    for row in board:
        for n in row:
            if n > 0:
                s += n
    return (s * num)


def won(boards):
    ret = 0
    for board in boards:
        colSum = [0 for i in range(5)]
        for row in board:
            if max(row) < 0:
                return (board, ret)
            for i in range(len(row)):
                if row[i] < 0:
                    colSum[i] += 1
        if max(colSum) == 5:
            return (board, ret)
        ret += 1
    return (None, ret)

day1printed = False

for num in numlist:
    for board in boards:
        for row in board:
            for i in range(len(row)):
                if row[i] == num:
                    row[i] = -row[i]-1 #for the zero
    #board checked

    winner, index = won(boards)

    while winner != None:
        if not day1printed:
            print("Day 4a:", getRes(winner, num))
            day1printed = True

        boards = boards[:index] + boards[index+1:]
        if len(boards) == 0:
            print("Day 4b:", getRes(winner, num))
            break
        winner, index = won(boards)

