n = int(input())
a = list(map(int, input().split()))
dem = 0
for x in a:
    if x % 2 == 0:
        dem += 1
print(dem)
