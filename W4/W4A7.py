n = int(input())

i = 2
largest = 0

while i <= n:
    if n % i == 0:
        largest = i
        n //= i
    else:
        i += 1

print(largest)