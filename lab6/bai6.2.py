# Nhập ma trận vuông từ bàn phím
n = int(input("Nhập kích thước của ma trận vuông: "))
ma_tran_vuong = []
print("Nhập các phần tử của ma trận:")
for i in range(n):
    hang = [float(x) for x in input(f"Nhập hàng {i+1} (các phần tử cách nhau bằng dấu cách): ").split()]
    ma_tran_vuong.append(hang)

# In ra ma trận vừa nhập
print("Ma trận vừa nhập:")
for hang in ma_tran_vuong:
    print(hang)