n = int(input("Nhập vào số nguyên n(n>10):"))
if n <= 10:
    print("Nhập sai!!! , vui lòng nhập lại:")
else:
    a = 0
    S = 0
    while a<n:
        S += a*(a + 1)*(a + 2 )
        a+=1
print("S=",S)
