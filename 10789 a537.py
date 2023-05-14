from collections import Counter

numList = []
for i in range(1,2001):
    count = 0
    for j in range(1,i):
        if i%j ==0:
            count+=1
    if count == 1:
        numList.append(i)
t = int(input())
ansList = []
for a in range(t):
    c = Counter(input())
    

    tempAnsList = []
    maxV = 1
    for k,v in c.items():
        if v in numList:
            # if v > maxV:
            #     tempAnsList = [k]
            #     maxV = v
            # elif v == maxV:
                tempAnsList.append(k)
    ansList.append(tempAnsList)


count = 0
for i in ansList:
    count +=1
    temp = ""
    for k in sorted(i) :
        temp+=k
    if temp == "":
        temp = "empty"
    print(f"Case {count}: {temp}")
