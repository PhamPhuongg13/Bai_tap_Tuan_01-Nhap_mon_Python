n = int(input())
a = n // 3600
b = n % 3600 // 60
c = n % 60
print(f"{a}:{b}:{c}")
