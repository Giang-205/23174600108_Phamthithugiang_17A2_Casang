bi = int(input("Nhập số lượng bi cần rút: "))
tong_so_bi = 50
bi_do = 20
bi_xanh = 15
bi_vang = 15

# tat ca la bi do:
xac_suat_bi_do = (bi_do / tong_so_bi) ** bi

# it nhat 1 bi xanh:
xac_suat_khong_lay_duoc_xanh = (35 / tong_so_bi) ** bi
xac_suat_lay_duoc_1_xanh = 1 - xac_suat_khong_lay_duoc_xanh

# dung 2 vien vang:
xac_suat_lay_duoc_dung_2_vang = (15 / tong_so_bi) * ((bi_vang - 1) / (tong_so_bi - 1)) * ((35 / 48) ** (bi - 2))

print("Xác xuất rút ra tát cả đều là bi đỏ: {:.4f}".format(xac_suat_bi_do))
print("Xác suất rút ra ít nhất 1 viên là bi xanh: {:.4f}".format(xac_suat_lay_duoc_1_xanh))
print("Xác suất rút ra đúng 2 viên bi vàng: {:.4f}".format(xac_suat_lay_duoc_dung_2_vang))