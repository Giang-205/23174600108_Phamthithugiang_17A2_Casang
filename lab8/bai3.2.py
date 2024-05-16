def tong_lap_phuong(n):
    tong = 0
    for chu_so in str(n):
        tong += int(chu_so) ** 3
    return tong

def la_so_armstrong(n):
    return n == tong_lap_phuong(n)

def in_so_armstrong():
    for num in range(1, 1000): 
        if la_so_armstrong(num):
            print(num, "là số Armstrong.")
print("123 có phải là số Armstrong?", la_so_armstrong(123))
print("153 có phải là số Armstrong?", la_so_armstrong(153))
print("Các số Armstrong từ 1 đến 999:")
in_so_armstrong()
