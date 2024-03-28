# câu b
n = int(input("Nhập số n:"))
if n <= 0 :
    n = int(input("Nhập sai!!! , Vui lòng nhập số nguyên dương:"))
s2 = sum(1/i for i in range(1,n+1))
print("Tổng s2 =",s2)


