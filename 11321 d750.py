from collections import defaultdict
while True:
    ori = input()
    if ori == "0 0":
        print(ori)
        break
    n = int(ori.split(" ")[0])
    m = int(ori.split(" ")[1])
    dict1 = defaultdict(list)
    remainList =[]
    for i in range(n):
        temp = int(input())
        tempType = temp%m
        if temp < 0 :
            tempType-=m
        if tempType not in remainList:
            remainList.append(tempType)
        if dict1[tempType] == []:
            dict1[tempType] = [[],[]]
        if temp % 2 == 0:
            dict1[tempType][0].append(temp)#even
        else:
            dict1[tempType][1].append(temp)#odd

    print(n,m)
    for i in sorted(remainList):
        for j in sorted(dict1[i][1],reverse=True):
            print(j)
        for j in sorted(dict1[i][0]):
            print(j)
