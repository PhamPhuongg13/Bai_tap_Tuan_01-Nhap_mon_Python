n = int(input())

while n <= 0:
    n = int(input())

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("true")
else:
    print("false")