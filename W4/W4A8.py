n = int(input())

count = 0

while True:
    temp = n
    reverse = 0

    while temp > 0:
        reverse = reverse * 10 + temp % 10
        temp //= 10

    if n == reverse:
        break

    n += reverse
    count += 1

print(count, n)