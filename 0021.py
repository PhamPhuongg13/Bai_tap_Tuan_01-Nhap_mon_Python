n = int(input())
if n <= 1:
    tien = n * 12000
elif n <= 30:
    tien = 12000 + (n - 1) * 10000
else:
    tien = 12000 + 29 * 10000 + (n - 30) * 9000
print(tien)
