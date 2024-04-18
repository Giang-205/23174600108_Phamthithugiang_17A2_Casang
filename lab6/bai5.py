danh_sach = input("Nhập dãy số, cách nhau bằng dấu cách: ").split()
danh_sach = [int(x) for x in danh_sach]
if len(danh_sach) < 2:
    print("Dãy số không đủ phần tử để tạo thành cấp số cộng.")
else:
    sai_so = danh_sach[1] - danh_sach[0]
    la_csc = True
    for i in range(2, len(danh_sach)):
        if danh_sach[i] - danh_sach[i-1] != sai_so:
            la_csc = False
            break
    if la_csc:
        print("Dãy số tạo thành cấp số cộng:", danh_sach)
    else:
        print("Dãy số không tạo thành cấp số cộng.")
