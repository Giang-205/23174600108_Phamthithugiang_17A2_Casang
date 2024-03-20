#Nhập vào điểm số của một bài ktra , in ra một thông báo tương ứng theo quy tắc
diem = float(input("Nhập điểm số:"))
if 0 <= diem < 5:
    print("Điểm kém")
if 5<= diem < 7:
    print("Điểm trung bình")
if 7 <= diem < 8.5:
    print("Điểm khá")
if 8.5 <= diem < 10:
    print("Điểm tốt")
else:
    print("Điểm không hợp lệ, nhập lại từ 0 đến 10")