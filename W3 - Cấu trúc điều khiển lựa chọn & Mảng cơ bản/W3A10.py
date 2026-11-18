a, b, c, d = map(int, input().split())
lon_nhat = a
if b > lon_nhat:
    lon_nhat = b
if c > lon_nhat:
    lon_nhat = c
if d > lon_nhat:
    lon_nhat = d
print(lon_nhat)
