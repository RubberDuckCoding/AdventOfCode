inc = 0
incl = 0
vals = [int(input())]

while True:

    val = input()
    if val == '':
        break
    vals.append(int(val))

    i = len(vals)-1
    
    s1=0
    s2=0
    if(len(vals)) >= 4:
        s1 = sum(vals[-4:-1])
        s2 = sum(vals[-3:])

    if s2 > s1:
        incl+=1

    if vals[-2] < vals[-1]:
        inc += 1

print("Day 1a:",inc)
print("Day 1b:",incl)
