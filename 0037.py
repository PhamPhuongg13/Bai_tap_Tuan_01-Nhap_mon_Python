m, n = map(int, input().split())
tu = m
mau = n
while n != 0:
    m, n = n, m % n
print(f"{tu // m}/{mau // m}")
