#Viết một chương trình Python nhận đầu vào là một số nguyên dương , và sau đó chuyển đổi nó sang số nhị phân
chuoi = ""
n = int(input("Nhập vào số nguyên: "))
if n < 0:
    print("Nhập lại số khác")
else:
    while n > 0:
        phan_du = n % 2
        chuoi = str(phan_du) + chuoi
        n = n // 2
    print("Chuyển số từ số nguyên dương sang hệ nhị phân :", chuoi)