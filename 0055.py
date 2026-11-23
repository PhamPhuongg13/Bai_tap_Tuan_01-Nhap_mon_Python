def second_maxi(numbers):
    if len(numbers) < 2:
        return None

    maxi = numbers[0]
    second_maxi = None

    for i in range(1, len(numbers)):
        cur = numbers[i]

        if cur > maxi:
            second_maxi = maxi
            maxi = cur
        elif cur < maxi and (second_maxi is None or cur > second_maxi):
            second_maxi = cur

    return second_maxi

numbers = list(map(int, input().split()))
result = second_maxi(numbers)

if result is None:
    print("-")
else:
    print(result)