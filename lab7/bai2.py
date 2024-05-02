thong_tin_sinh_vien = {}
for i in range(1, 11):
    ten = input(f"Nhập tên của sinh viên thứ {i}: ")
    diem_thi = float(input(f"Nhập điểm thi của sinh viên {ten}: "))
    thong_tin_sinh_vien[ten] = diem_thi

# Tạo từ điển xếp loại học lực của từng sinh viên
xep_loai_hoc_luc = {}
for ten, diem_thi in thong_tin_sinh_vien.items():
    if diem_thi < 4.0:
        xep_loai_hoc_luc[ten] = 'F'
    elif diem_thi < 5.5:
        xep_loai_hoc_luc[ten] = 'D'
    elif diem_thi < 7.0:
        xep_loai_hoc_luc[ten] = 'C'
    elif diem_thi < 8.5:
        xep_loai_hoc_luc[ten] = 'B'
    else:
        xep_loai_hoc_luc[ten] = 'A'

so_luong_loai_hoc_luc = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
for loai in xep_loai_hoc_luc.values():
    so_luong_loai_hoc_luc[loai] += 1

print("\nXếp loại học lực của từng sinh viên:")
for ten, xep_loai in xep_loai_hoc_luc.items():
    print(f"{ten}: {xep_loai}")

# In thống kê số lượng sinh viên ở mỗi loại học lực
print("\nThống kê số lượng sinh viên ở mỗi loại học lực:")
for loai, so_luong in so_luong_loai_hoc_luc.items():
    print(f"{loai}: {so_luong}")
