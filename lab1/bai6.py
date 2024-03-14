import math
x1, y1, x2, y2 = map(float,input("nhập các số: ").split())
a = ( x1 , y1 )
b = (x2,y2)
A = (x1+x2, y1+y2)
B = (x1-x2, y1-y2)

C = math.sqrt(x1**2 + y1**2)
D = math.sqrt(x2**2 + y2**2)

tich_co_huong = (x1 * x2) + (y1 * y2)
tich_do_dai = C * D
cos_hop_giua = tich_co_huong / tich_do_dai

print("phép cộng 2 vecto là:",A)
print("phép trừ 2 vecto là:",B)
print("độ dài vecto a:",C)
print("độ dài vecto b:",D)
print("Cos giữa 2 vecto = {:.2f} ".format(cos_hop_giua))