m, n = map(int, input().split())
dem = 0
tong = 0
for i in range(m, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        dem += 1
    if i % 2 == 0:
        tong += i
print(dem, tong)
