gia_ve_mot_nguoi = 120000
so_nguoi = int(input("Nhập số lượng người:"))
#Áp dụng giảm giá
if 2<= so_nguoi <=4:
    giam_gia = so_nguoi*gia_ve_mot_nguoi*(1-0.05)
elif 4 < so_nguoi <=10:
    giam_gia = so_nguoi*gia_ve_mot_nguoi*(1-0.1)
elif so_nguoi>10:
    giam_gia = so_nguoi*gia_ve_mot_nguoi*(1-0.2)
else:
    so_nguoi ==1
    giam_gia = 0
print("tổng số tiền phải trả:",giam_gia,"đồng.")
