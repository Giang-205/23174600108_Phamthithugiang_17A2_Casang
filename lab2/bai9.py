# Kiểm tra vị trị tương đối giữa một đường thẳng và một đường tròn trong không gian 2 chiều
import math
#Nhập thông số của đường thẳng
a, b = map(float, input("Nhập hệ số góc và hệ số tự do của đường thẳng: ").split()) 
#Nhập thông số của đường tròn
x, y = map(float, input("Nhập tọa độ tâm của đường tròn (x , y): ").split())
r = float(input("Nhập bán kính của đường tròn:"))
khoang_cach = abs(a*x + b*y +b) / math.sqrt(a**2 + b**2)
if khoang_cach < r:
    print("Đường thẳng cắt đường tròn")
elif khoang_cach == r:
    print("Đường thẳng tiếp xúc đường tròn")
elif khoang_cach > r:
    print("Đường thẳng nằm ngoài đường tròn")
else:
    print("Đường thẳng nằm trong đường tròn")