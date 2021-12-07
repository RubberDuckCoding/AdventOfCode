line = (input()).split()
vals = []

while len(line):
    vals.append(line[0])
    line=(input()).split()
    pass

def getEG(vals):
    output = [0 for i in range(len(vals[0]))]
    for num in vals:
        for i in range(len(num)):
            if num[i] == '1':
                output[i]+=1

    eps = ""
    gam = ""
    for v in output:
        if v >= len(vals)/2: #half or more ones
            gam += "1"
            eps += "0"
        else:
            gam += "0"
            eps += "1"
    return (eps,gam)


eps,gam=getEG(vals)
print("Day 3a:",int(gam,2)*int(eps,2))

oxfilter = vals.copy()
cofilter = vals.copy()

#find o2 filter
for i in range(len(gam)):
    if len(oxfilter) > 1:
        eps,gam=getEG(oxfilter)
        diff = 0
        for j in range(len(oxfilter)):
            j = j-diff
            if oxfilter[j][i] != gam[i]:
                oxfilter = oxfilter[:j] + oxfilter[j+1:]
                diff +=1
            if len(oxfilter)==1:
                break
    else:
        break

#find co2 filter
eps,gam=getEG(vals)
for i in range(len(eps)):
    if len(cofilter) > 1:
        eps,gam=getEG(cofilter)
        diff = 0
        for j in range(len(cofilter)):
            j = j-diff
            if cofilter[j][i] != eps[i]:
                cofilter = cofilter[:j] + cofilter[j+1:]
                diff += 1
            if len(cofilter)==1:
                break
    else:
        break


print("Day 3b:",int(oxfilter[0],2)*int(cofilter[0],2))
