n = int(input())
a = n // 5000
n %= 5000
b = n // 2000
n %= 2000
c = n // 1000
print(a, b, c)
