chuoi_1 = input("Nhập chuỗi thứ nhất: ")
chuoi_2 = input("Nhập chuỗi thứ hai: ")
so_luong_ky_tu_khac_nhau = abs(len(chuoi_1) - len(chuoi_2))
for ky_tu_1, ky_tu_2 in zip(chuoi_1, chuoi_2):
    if ky_tu_1 != ky_tu_2:
        so_luong_ky_tu_khac_nhau += 1
if so_luong_ky_tu_khac_nhau <= 1:
    print("Có thể thay đổi chuỗi 1 thành chuỗi 2.")
else:
    print("Không thể thay đổi chuỗi 1 thành chuỗi 2.")
