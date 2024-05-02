ten_sinh_vien = input("Tên của sinh viên: ")
N = int(input("Nhập số nguyên N: "))
tu_dien_sinh_vien = {ten_sinh_vien:{x: x**3 for x in range(1, N+1)}}
print(tu_dien_sinh_vien)
