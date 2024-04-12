while True:
    chuoi = input("Nhập chuỗi có độ dài ít nhất 3 ký tự: ")
    if len(chuoi) >= 3:
        break
    else:
        print("Chuỗi phải có ít nhất 3 ký tự!")
chuoi_con = chuoi[-3:]
print("Chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự:", chuoi_con)