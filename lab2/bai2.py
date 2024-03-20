#Nhập vào một số nguyên , yêu cầu xuất ra chữ số hàng nghìn của số đó,nếu không có thì xuất ra 0
n = int(input("Nhap vao so nguyen:"))
chu_so_hang_nghin = n//1000
if chu_so_hang_nghin == 0:
    print("so khong co chu so hang nghin")
elif 0<chu_so_hang_nghin<=9:
    print("chu so hang nghin la:",chu_so_hang_nghin)
else:
    phan_du = chu_so_hang_nghin % 10
    if phan_du == 0:
        print("chu so hang nghin la:",0)
    else:
        print("chu so hang nghin la:",phan_du)

