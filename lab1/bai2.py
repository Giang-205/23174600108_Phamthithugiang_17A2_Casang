#Viết chương trình quản lí thông tin sách trong 1 thư viện
soluongsach=int(input("Nhập số lượng sách:"))
masach=int(input("Nhập mã sách:"))
tensach=input("Nhập tên sách:")
tacgia=input("Nhập tên tác giả:")
namsuatban=int(input("Nhập năm suất bản:"))
print("---------------------------")
print(f"""Thư viện ĐHKTKTCN có {soluongsach} sách {tensach} với mã số {masach}.Cuốn sách của tác giả {tacgia} được xuất bản vào năm {namsuatban}""")