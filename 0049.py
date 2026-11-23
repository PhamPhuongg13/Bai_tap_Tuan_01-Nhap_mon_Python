n = int(input())
lst = list(map(int, input().split()))

newval = lst[0]
pos = 0

for i in range(1, n):
    if lst[i] > newval:
        newval = lst[i]
        pos = i

print(newval, pos)