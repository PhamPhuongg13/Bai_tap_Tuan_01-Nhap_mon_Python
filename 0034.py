m, n = map(int, input().split())
dem = 0
for i in range(m, n + 1):
    dem_uoc = 0
    for j in range(1, i + 1):
        if i % j == 0:
            dem_uoc += 1
    if dem_uoc == 2:
        print(i, end = " ")
        dem += 1
if dem == 0:
    print("-")
