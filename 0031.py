m, n = map(int, input().split())
dem = 0
for i in range(m, n + 1):
    if i % 3 == 0:
        dem += 1
print(dem)
