numbers = list(map(int, input().split()))

total = 0
count = 0

for number in numbers:
    if number >= 0:
        root = 0

        while root * root < number:
            root = root + 1

        if root * root == number:
            total = total + number
            count = count + 1

if count == 0:
    print("-")
else:
    average = total / count
    print("{:.1f}".format(average))