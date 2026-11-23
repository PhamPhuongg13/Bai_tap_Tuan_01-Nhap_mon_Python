n, m = map(int, input().split())

check = False

for ga in range(n + 1):
    cho = n - ga

    if ga * 2 + cho * 4 == m:
        print(ga, cho)
        check = True
        break

if not check:
    print("invalid")