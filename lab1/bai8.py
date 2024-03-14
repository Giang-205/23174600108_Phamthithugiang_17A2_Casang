import math
x, z = map(float,input("nhập các giá trị: ").split())
tu = x**2*math.sin(z)+ math.sqrt(abs(x))
mau = math.log(z) + math.exp(x-1)
f = mau/ tu + math.atan(x**2)
print("giá trị của biểu thức là: %0.2f"%f) 