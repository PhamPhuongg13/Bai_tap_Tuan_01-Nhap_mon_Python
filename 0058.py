n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

newlst = []

for i in lst:
    if i not in newlst:
        newlst.append(i)

for i in newlst:
    count = 0
    for j in lst:
        if i == j:
            count += 1
    print(i, count)