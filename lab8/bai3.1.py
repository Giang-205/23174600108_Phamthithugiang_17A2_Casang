def tong_lap_phuong(n):
    tong = 0
    for chu_so in str(n):
        tong += int(chu_so) ** 3
    return tong
n = int(input("nhập số n :"))
print("Tổng của các lập phương của các chữ số riêng lẻ của", n, "là:", tong_lap_phuong(n))
