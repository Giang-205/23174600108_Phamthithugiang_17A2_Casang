#Viết chương trình nhập số n là sô nguyên dương , n<=0 thì yêu cầu nhập lại
# câu a
n = int(input("Nhập số n:"))
if n <= 0 :
    n = int(input("Nhập sai!!! , Vui lòng nhập số nguyên dương:"))
s1 = sum(range(1, n+1))
print("Tổng s1 =",s1)


