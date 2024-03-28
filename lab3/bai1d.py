# Câu d
import math 
n = int(input("Nhập số n:"))
if n <= 0 :
    n = int(input("Nhập sai!!! , Vui lòng nhập số nguyên dương:"))
s4 = sum(((-1)**(i+1))/i for i in range(1,n+1))
print("Tổng s4 =",s4)
