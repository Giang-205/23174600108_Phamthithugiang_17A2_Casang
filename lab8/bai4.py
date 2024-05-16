def tong_uoc_so_chinh(n):
    tong = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            tong += i
    return tong

so_nguyen = int(input("Nhập số nguyên :"))
print("Tổng của các ước số chính của", so_nguyen, "là:", tong_uoc_so_chinh(so_nguyen))


