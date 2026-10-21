x = input()
so_nut = sum(map(int, x)) % 10
print(so_nut)
if so_nut == 9:
    print("may man")
else:
    print("chua may man")
