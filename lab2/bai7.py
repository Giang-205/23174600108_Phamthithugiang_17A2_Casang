# Tính chỉ số BMI dựa trên chiều cao và cân nặng
chieu_cao = float(input("Nhập chiều cao của bạn:"))
can_nang = float(input("Nhập cân nặng của bạn:"))
#Chỉ số BMI
bmi = can_nang / (chieu_cao**2)
#Phân loại
if bmi < 18.5:
    phan_loai = "Gầy"
elif 18.5 <= bmi <=24.9:
    phan_loai = "Bình Thường"
elif 25.0 <= bmi <=29.9:
    phan_loai = "Hơi béo"
else:
    phan_loai = "Béo"
print("Chỉ số BMI của bạn là:", bmi)
print("Phân loại BMI của bạn là:",phan_loai)
 
