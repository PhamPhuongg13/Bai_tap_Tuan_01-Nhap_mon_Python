n = int(input())

check = False

for i in range(n):
    a = int(input())
    if a == 42:
        check = True

if check:
    print("I've found the meaning of life!")
else:
    print("It's a joke!")