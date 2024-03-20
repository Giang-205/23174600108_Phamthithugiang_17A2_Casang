a,b = map(int,input("Nhập vào hệ số của phương trình: ").split())
if a==0:
    if b==0:
        print("Phuong trinh bac nhat co vo so nghiem")
    else:
        print("phuong trinh bac nhat vo nghiem")
else:
    x = -a/b
    print("Phuong trinh bac nhat co nghiem la x=",x)