while True:
    chuoi = input("Nhập chuỗi có độ dài ít nhất 10 ký tự: ")
    if len(chuoi) >= 10:
        break
    else:
        print("Chuỗi phải có ít nhất 10 ký tự!")
chuoi_con = chuoi[4:9]
print("Chuỗi ký tự con từ vị trí thứ 5 gồm 5 ký tự:", chuoi_con)