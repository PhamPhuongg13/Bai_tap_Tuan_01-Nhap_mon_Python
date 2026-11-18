n, x = map(int, input().split())
a = list(map(int, input().split()))
vi_tri = -1
for i in range(n):
    if a[i] == x:
        vi_tri = i
        break
if vi_tri == -1:
    print("No")
else:
    print("Yes")
    print(vi_tri)
