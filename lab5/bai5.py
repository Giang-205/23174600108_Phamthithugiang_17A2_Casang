str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")
chuoi_gop = ""
min_length = 0
len1 = len(str1)
len2 = len(str2)
while len1 > min_length or len2 > min_length:
    if len1 > min_length :
        chuoi_gop += str1[min_length] + "-"
    if len2 >  min_length:
        chuoi_gop += str2[min_length] + "-"
    min_length += 1
print("Ký tự sau khi trộn là:" , chuoi_gop [:-1])