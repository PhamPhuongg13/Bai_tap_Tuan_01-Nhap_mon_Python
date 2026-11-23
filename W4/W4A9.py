n = int(input())

count = 0

for i in range(1, n + 1):
    square = i * i
    temp = square
    digits = []

    check = True

    while temp > 0:
        digit = temp % 10

        if digit in digits:
            check = False

        digits.append(digit)
        temp //= 10

    if check:
        print(square, end = " ")
        count += 1

if count == 0:
    print("(no number)")