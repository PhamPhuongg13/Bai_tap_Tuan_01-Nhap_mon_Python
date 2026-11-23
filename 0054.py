lst = list(map(int, input().split()))
x = None

for i in lst:
    if i < 0 and (x is None or x < i):
        x = i

if x is None:
    print("-")
else:
    print(x)