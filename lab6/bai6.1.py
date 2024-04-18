# Nhập ma trận từ bàn phím
ma_tran = []
m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))
print("Nhập các phần tử của ma trận:")
for i in range(m):
    hang = []
    for j in range(n):
        hang.append(float(input(f"Nhập phần tử [{i+1}, {j+1}]: ")))
    ma_tran.append(hang)
print("Ma trận vừa nhập:")
for hang in ma_tran:
    print(hang)

# Tính tổng của tất cả các phần tử trong ma trận
tong = 0
for hang in ma_tran:
    tong += sum(hang)
print("Tổng của ma trận:", tong)

# Nhập ma trận thứ hai từ bàn phím
ma_tran2 = []
m2 = int(input("Nhập số hàng của ma trận thứ hai: "))
n2 = int(input("Nhập số cột của ma trận thứ hai: "))
print("Nhập các phần tử của ma trận thứ hai:")
for i in range(m2):
    hang = []
    for j in range(n2):
        hang.append(float(input(f"Nhập phần tử [{i+1}, {j+1}]: ")))
    ma_tran2.append(hang)

# Tính tích của hai ma trận
if n != m2:
    print("Hai ma trận không thể nhân với nhau.")
else:
    k = len(ma_tran2)
    ma_tran_tich = []
    for i in range(m):
        hang_moi = []
        for j in range(k):
            hang_moi.append(sum(ma_tran[i][l] * ma_tran2[l][j] for l in range(k)))
        ma_tran_tich.append(hang_moi)

    print("Ma trận tích của hai ma trận:")
    for hang in ma_tran_tich:
        print(hang)

# Tạo ma trận chuyển vị của ma trận ban đầu và in ra
print("Ma trận chuyển vị của ma trận ban đầu:")
ma_tran_chuyen_vi = [[ma_tran[j][i] for j in range(m)] for i in range(n)]
for hang in ma_tran_chuyen_vi:
    print(hang)
