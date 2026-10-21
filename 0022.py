n = int(input())
if n <= 50:
    tien = n * 600
elif n <= 100:
    tien = 50 * 600 + (n - 50) * 800
elif n <= 200:
    tien = 50 * 600 + 50 * 800 + (n - 100) * 1100
else:
    tien = 50 * 600 + 50 * 800 + 100 * 1100 + (n - 200) * 1500
print(tien)
