k = int(input())
dem = 0
n = 2
while dem < k:
    dem_uoc = 0
    for i in range(1, n + 1):
        if n % i == 0:
            dem_uoc += 1
    if dem_uoc == 2:
        print(n, end = " ")
        dem += 1
    n += 1
