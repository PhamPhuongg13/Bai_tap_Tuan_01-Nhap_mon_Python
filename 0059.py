n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

newval = lst[0]
max_count = 0

for i in lst:
    count = 0
    for j in lst:
        if i == j:
            count += 1

    if count > max_count:
        max_count = count
        newval = i

print(newval, max_count)