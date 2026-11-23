n = int(input())

max_count = 0
result = 1

for i in range(1, n + 1):
    temp = i
    count = 0

    while temp != 1:
        if temp % 2 == 0:
            temp //= 2
        else:
            temp = temp * 3 + 1

        count += 1

    if count > max_count:
        max_count = count
        result = i

print(result, max_count)