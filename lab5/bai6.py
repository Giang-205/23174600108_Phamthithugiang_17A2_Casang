chuoi = input("Nhập chuỗi: ")
so_ky_tu_dac_biet = 0
ky_tu_dac_biet_dict = {}
tong_so_ky_tu = len(chuoi)
for char in chuoi:
    if not char.isalnum():
        so_ky_tu_dac_biet += 1
        if char in ky_tu_dac_biet_dict:
            ky_tu_dac_biet_dict[char] += 1
        else:
            ky_tu_dac_biet_dict[char] = 1
if so_ky_tu_dac_biet > 0:
    print("Các ký tự đặc biệt trong chuỗi:")
    for char, count in ky_tu_dac_biet_dict.items():
        ty_le = (count / tong_so_ky_tu) * 100
        print(f"- '{char}': {ty_le:.2f}% (xuất hiện {count} lần)")
else:
    print("Không có ký tự đặc biệt trong chuỗi.")
