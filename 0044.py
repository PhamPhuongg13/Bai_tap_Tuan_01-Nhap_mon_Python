n = int(input())
a = list(map(int, input().split()))
tong = 0
for i in range(0, n, 2):
    tong += a[i]
print(tong)
