kho = {
 "banana": 6,
 "apple": 5,
 "orange": 32,
 "pear": 15
}
gia_tien = {
 "banana": 4,
 "apple": 2,
 "orange": 1.5,
 "pear": 3
}
# Tạo từ điển cho kho hàng và giá tiền
kho = {
    "banana": 6,
    "apple": 5,
    "orange": 32,
    "pear": 15
}

gia_tien = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
mua_hang = {}
print("Nhập số lượng mua cho từng mặt hàng (nhập 0 nếu không mua):")
for mat_hang in kho:
    so_luong = int(input(f"Số lượng {mat_hang}: "))
    if so_luong > 0:
        if so_luong <= kho[mat_hang]:
            mua_hang[mat_hang] = so_luong
        else:
            print(f"Không đủ hàng trong kho cho {mat_hang}. Hiện chỉ có {kho[mat_hang]}.")


hoa_don = {}
tong_tien = 0

for mat_hang, so_luong in mua_hang.items():
    if mat_hang in kho and kho[mat_hang] >= so_luong:
        don_gia = gia_tien[mat_hang]
        so_tien = don_gia * so_luong
        tong_tien += so_tien
        hoa_don[mat_hang] = {
            "so_luong": so_luong,
            "don_gia": don_gia,
            "so_tien": so_tien
        }
        kho[mat_hang] -= so_luong
    else:
        print(f"Không đủ số lượng {mat_hang} trong kho.")

# In hóa đơn mua hàng
print("Hóa đơn mua hàng:")
for mat_hang, thong_tin in hoa_don.items():
    print(f"Mặt hàng: {mat_hang}")
    print(f"Số lượng: {thong_tin['so_luong']}")
    print(f"Đơn giá: {thong_tin['don_gia']}")
    print(f"Số tiền: {thong_tin['so_tien']}")
    print()

print(f"Tổng số tiền của hóa đơn: {tong_tien}")

# In lại số lượng của các mặt hàng trong kho
print("\nSố lượng của các mặt hàng trong kho sau khi mua hàng:")
for mat_hang, so_luong in kho.items():
    print(f"{mat_hang}: {so_luong}")
