# câu c
import math 
n = int(input("Nhập số n:"))
if n <= 0 :
    n = int(input("Nhập sai!!! , Vui lòng nhập số nguyên dương:"))
s3 = sum(1/ math.sqrt(2*i) for i in range(1,n+1))
print("Tổng s3 =",s3)
