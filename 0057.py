lst = []

while True:
    try:
        n = int(input())
        lst.append(n)
    except EOFError:
        break

newlst = []

for i in lst:
    if i not in newlst:
        newlst.append(i)

print(len(newlst))