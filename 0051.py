def is_prime(n):
    if n < 2:
        return False
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True

lst = list(map(int, input().split()))

tong = 0
count = 0

for i in lst:
    if is_prime(i):
        print(i, end = " ")
        tong += i
        count += 1

if count == 0:
    print("-")
else:
    print()

print(tong)