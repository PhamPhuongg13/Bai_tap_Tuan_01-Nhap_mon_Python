m, n = map(int, input().split())

while n != 0:
    r = m % n
    m = n
    n = r

print(m)