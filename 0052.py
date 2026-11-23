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
        tong += i
        count += 1

if count > 0:
    print(f"{tong/count:.2f}")
else:
    print("-")