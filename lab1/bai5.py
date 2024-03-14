U = 220
I = 1.5
sogio = int(input("Nhập số giờ sử dụng máy lọc không khí:"))
#Tính công suất tiêu thụ
P = U*I
#Tính tiền điện
KWh = P/1000
sotientra = 5000*KWh*sogio
#In ra màn hình kết quả
print("-------------------------------")
print("Số tiền gia đình đó phải trả cho máy lọc không khí là:", sotientra)
