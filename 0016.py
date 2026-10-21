tb_hk1, tb_hk2 = map(float, input().split())
tb_cn = (tb_hk1 + 2 * tb_hk2) / 3
print(f"{tb_cn:.1f}")
if tb_cn >= 8:
    print("Gioi")
elif tb_cn >= 6.5:
    print("Kha")
elif tb_cn >= 5:
    print("Trung binh")
elif tb_cn >= 3.5:
    print("Yeu")
else:
    print("Kem")
