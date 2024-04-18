dai_so = input("Nhập dãy số: ").split()

dai_so = [float(x) for x in dai_so if x.replace('.', '', 1).isdigit()]

if dai_so:
    so_lon_nhat = dai_so[0]
    so_nho_nhat = dai_so[0]
    for i in dai_so:
        if i > so_lon_nhat:
            so_lon_nhat = i
        if i < so_nho_nhat:
            so_nho_nhat = i
    print("Số lớn nhất trong dãy số:", so_lon_nhat)
    print("Số nhỏ nhất trong dãy số:", so_nho_nhat)
else:
    print("Dãy số trống hoặc không hợp lệ.")
