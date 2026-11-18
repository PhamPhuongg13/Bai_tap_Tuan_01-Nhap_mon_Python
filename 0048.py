n = int(input())
a = list(map(int, input().split()))
dem = 0
tong = 0
for x in a:
    if x % 5 == 0:
        print(x, end = " ")
        tong += x
        dem += 1
if dem == 0:
    print("-")
else:
    print()
print(tong)
