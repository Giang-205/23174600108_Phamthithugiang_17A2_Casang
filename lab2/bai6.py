a, b, c = map(int,input("Nhập các số a,b,c: ").split())
so_lon_nhat = max(a,b,c)
if a == so_lon_nhat:
    if b > c :
        so_lon_thu_hai = b
    else:
        so_lon_thu_hai = c
elif b == so_lon_nhat:
    if a> c:
        so_lon_thu_hai = a
    else:
        so_lon_thu_hai = c
else:
    if a> b:
        so_lon_thu_hai = a
    else:
        so_lon_thu_hai = b
        print("số lớn thứ hai là:", so_lon_thu_hai)