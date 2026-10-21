thang, nam = map(int, input().split())
if thang == 2:
    if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
        print(29)
    else:
        print(28)
elif thang in (4, 6, 9, 11):
    print(30)
else:
    print(31)
