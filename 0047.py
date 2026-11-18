n = int(input())
a = list(map(int, input().split()))
dem_duong = 0
dem_am = 0
for x in a:
    if x > 0:
        dem_duong += 1
    elif x < 0:
        dem_am += 1
print(dem_duong, dem_am)
if dem_duong == 0:
    print("-")
else:
    for x in a:
        if x > 0:
            print(x, end = " ")
    print()
if dem_am == 0:
    print("-")
else:
    for x in a:
        if x < 0:
            print(x, end = " ")
    print()
