n = int(input())
a = list(map(int, input().split()))
dem = 0
tong = 0
for x in a:
    if x % 2 == 0:
        tong += x
        dem += 1
if dem == 0:
    print("-")
else:
    print(tong)
