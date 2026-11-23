a, b = map(int, input().split())

tong1 = 0
tong2 = 0

for i in range(1, a):
    if a % i == 0:
        tong1 += i

for i in range(1, b):
    if b % i == 0:
        tong2 += i

if tong1 == b and tong2 == a:
    print("true")
else:
    print("false")