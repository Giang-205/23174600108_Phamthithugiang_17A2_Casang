#Viết một chương trình Python nhận đầu vào là hai chuỗi ký tự str1 và str2, sau đó tìm ra chuỗi ký tự con chung có độ dài ngắn nhất của hai chuỗi này
chuoi_1 = input("Nhập chuỗi thứ nhất: ")
chuoi_2 = input("Nhập chuỗi thứ hai: ")

do_dai_1 = len(chuoi_1)
do_dai_2 = len(chuoi_2)
do_dai_chuoi_con_chung = [[0] * (do_dai_2 + 1) for _ in range(do_dai_1 + 1)]
do_dai_nho_nhat = float('inf')
chuoi_con_chung = ''

for i in range(1, do_dai_1 + 1):
    for j in range(1, do_dai_2 + 1):
        if chuoi_1[i - 1] == chuoi_2[j - 1]:
            do_dai_chuoi_con_chung[i][j] = do_dai_chuoi_con_chung[i - 1][j - 1] + 1
            if do_dai_chuoi_con_chung[i][j] < do_dai_nho_nhat:
                do_dai_nho_nhat = do_dai_chuoi_con_chung[i][j]
                chuoi_con_chung = chuoi_1[i - do_dai_nho_nhat:i]
        else:
            do_dai_chuoi_con_chung[i][j] = 0

if do_dai_nho_nhat > 0:
    print("Chuỗi con chung có độ dài ngắn nhất là:", chuoi_con_chung)
else:
    print("Không có chuỗi con chung nào.")





