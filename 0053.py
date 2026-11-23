def is_prime(n):
    if n < 2:
        return False
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            return False
    return True

lst = list(map(int, input().split()))
Var = None

for i in lst:
    if is_prime(i) and (Var is None or i > Var):
        Var = i

if Var is None:
    print("-")
else:
    print(Var)