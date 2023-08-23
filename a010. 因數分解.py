from collections import defaultdict

num = int(input())
d = defaultdict(int)
tempNum = 2
while num != 1:
    if num % tempNum == 0:
        d[str(tempNum)] += 1
        num /= tempNum
    else:
        tempNum+=1
l = []
for key,value in d.items():
    if value > 1:
        l.append(f"{key}^{value}")
    else:
        l.append(f"{key}")
print(" * ".join(l))

